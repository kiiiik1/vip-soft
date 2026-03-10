#!/usr/bin/env python3
"""
OpenClaw & ZeroClaw Money Making Guide HTML Converter
将Markdown文件转换为HTML格式
"""

import os
import sys
import markdown
from pathlib import Path

def convert_md_to_html(md_file_path, html_file_path):
    """
    将Markdown文件转换为HTML
    
    Args:
        md_file_path: Markdown文件路径
        html_file_path: 输出HTML文件路径
    """
    try:
        # 读取Markdown文件
        with open(md_file_path, 'r', encoding='utf-8') as md_file:
            md_content = md_file.read()
        
        # 转换Markdown为HTML
        html_content = markdown.markdown(
            md_content,
            extensions=[
                'markdown.extensions.tables',
                'markdown.extensions.toc',
                'markdown.extensions.codehilite',
                'markdown.extensions.fenced_code'
            ]
        )
        
        # 添加HTML样式
        html_template = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>{os.path.basename(md_file_path).replace('.md', '')}</title>
            <style>
                body {{
                    font-family: 'Arial', 'Microsoft YaHei', sans-serif;
                    line-height: 1.6;
                    margin: 0;
                    padding: 0;
                    color: #333;
                }}
                .container {{
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                h1, h2, h3, h4, h5, h6 {{
                    color: #2c3e50;
                    margin-top: 30px;
                    margin-bottom: 15px;
                }}
                h1 {{
                    text-align: center;
                    border-bottom: 3px solid #3498db;
                    padding-bottom: 10px;
                }}
                h2 {{
                    border-bottom: 2px solid #3498db;
                    padding-bottom: 5px;
                }}
                h3 {{
                    border-bottom: 1px solid #3498db;
                    padding-bottom: 3px;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    margin: 20px 0;
                }}
                th, td {{
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                }}
                th {{
                    background-color: #f2f2f2;
                    font-weight: bold;
                }}
                code {{
                    background-color: #f4f4f4;
                    padding: 2px 4px;
                    border-radius: 3px;
                    font-family: 'Courier New', monospace;
                }}
                pre {{
                    background-color: #f4f4f4;
                    padding: 15px;
                    border-radius: 5px;
                    overflow-x: auto;
                    margin: 15px 0;
                }}
                blockquote {{
                    border-left: 4px solid #3498db;
                    margin: 15px 0;
                    padding-left: 15px;
                    color: #666;
                }}
                ul, ol {{
                    margin: 15px 0;
                    padding-left: 20px;
                }}
                li {{
                    margin: 5px 0;
                }}
                .toc {{
                    background-color: #f8f9fa;
                    padding: 15px;
                    border-radius: 5px;
                    margin: 20px 0;
                }}
                .toc ul {{
                    list-style-type: none;
                    padding-left: 0;
                }}
                .toc a {{
                    text-decoration: none;
                    color: #3498db;
                }}
                .toc a:hover {{
                    text-decoration: underline;
                }}
                .price {{
                    background-color: #e8f5e8;
                    padding: 10px;
                    border-radius: 5px;
                    margin: 10px 0;
                }}
                .warning {{
                    background-color: #fff3cd;
                    padding: 10px;
                    border-radius: 5px;
                    margin: 10px 0;
                }}
                .success {{
                    background-color: #d4edda;
                    padding: 10px;
                    border-radius: 5px;
                    margin: 10px 0;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                {html_content}
            </div>
        </body>
        </html>
        """
        
        # 写入HTML文件
        with open(html_file_path, 'w', encoding='utf-8') as html_file:
            html_file.write(html_template)
        
        print(f"✅ 成功转换: {md_file_path} -> {html_file_path}")
        return True
        
    except Exception as e:
        print(f"❌ 转换失败: {e}")
        return False

def main():
    """主函数"""
    # 检查依赖
    try:
        import markdown
    except ImportError:
        print("❌ 缺少依赖: markdown")
        print("请安装依赖: pip3 install markdown")
        sys.exit(1)
    
    # 获取当前目录
    current_dir = Path(__file__).parent
    money_guide_dir = current_dir / "zeroclaw-money-guide"
    
    # 确保目录存在
    if not money_guide_dir.exists():
        print(f"❌ 目录不存在: {money_guide_dir}")
        sys.exit(1)
    
    # 源文件和目标文件
    md_files = {
        "OpenClaw_ZeroClaw_Money_Making_Secrets_EN.md": "OpenClaw_ZeroClaw_Money_Making_Secrets_EN.html",
        "OpenClaw_ZeroClaw_Money_Making_Secrets_CN.md": "OpenClaw_ZeroClaw_Money_Making_Secrets_CN.html"
    }
    
    # 创建输出目录
    output_dir = current_dir / "html-output"
    output_dir.mkdir(exist_ok=True)
    
    print("🚀 开始转换HTML文件...")
    
    # 转换所有文件
    success_count = 0
    for md_filename, html_filename in md_files.items():
        md_file_path = money_guide_dir / md_filename
        html_file_path = output_dir / html_filename
        
        if md_file_path.exists():
            if convert_md_to_html(md_file_path, html_file_path):
                success_count += 1
        else:
            print(f"❌ 文件不存在: {md_file_path}")
    
    print(f"\n📊 转换完成: {success_count}/{len(md_files)} 个文件成功转换")
    print(f"📁 HTML文件保存在: {output_dir.absolute()}")

if __name__ == "__main__":
    main()