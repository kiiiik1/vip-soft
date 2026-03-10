#!/usr/bin/env python3
"""
Free Online Search Skill
Uses DuckDuckGo HTML version for free web search
"""

import urllib.request
import urllib.parse
import re
import json
import sys

def search_duckduckgo(query, num_results=5):
    """Search using DuckDuckGo HTML version (no API key needed)"""
    try:
        # Encode query
        encoded_query = urllib.parse.quote_plus(query)
        
        # Use DuckDuckGo HTML search
        url = f"https://html.duckduckgo.com/html/?q={encoded_query}"
        
        # Create request with headers
        req = urllib.request.Request(
            url,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
        )
        
        # Make request
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8')
        
        # Extract results using regex
        results = []
        result_pattern = r'<a rel="nofollow" class="result__a" href="([^"]+)".*?>(.*?)</a>'
        
        matches = re.findall(result_pattern, html, re.DOTALL)
        
        for i, (url, title) in enumerate(matches[:num_results]):
            # Clean up title
            title = re.sub(r'<[^>]+>', '', title)
            title = title.strip()
            
            # Get snippet if available
            snippet_pattern = f'<a[^>]*{re.escape(url)}[^>]*>.*?</a>.*?<a[^>]*class="result__snippet"[^>]*>(.*?)</a>'
            snippet_match = re.search(snippet_pattern, html, re.DOTALL)
            snippet = snippet_match.group(1) if snippet_match else ""
            snippet = re.sub(r'<[^>]+>', '', snippet).strip()
            
            results.append({
                'title': title,
                'url': url,
                'snippet': snippet
            })
        
        return results
        
    except Exception as e:
        return [{'error': f'Search failed: {str(e)}'}]

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 search.py 'search query'")
        sys.exit(1)
    
    query = ' '.join(sys.argv[1:])
    results = search_duckduckgo(query)
    
    print(json.dumps(results, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()