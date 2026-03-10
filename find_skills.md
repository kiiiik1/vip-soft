# Find Skills Skill - 技能查找工具

## Description
提供技能查找和搜索功能，可以搜索已安装的技能文件，查找特定技能或列出所有可用技能。

## Usage
```bash
# 列出所有技能
python3 skills/find_skills.py --list

# 搜索特定技能
python3 skills/find_skills.py --search "search"

# 查找技能文件
python3 skills/find_skills.py --find "search.py"

# 获取技能详细信息
python3 skills/find_skills.py --info "search"
```

## Implementation
find_skills技能使用：
- Python文件系统操作
- 正则表达式匹配
- JSON格式输出

## Features
- 列出所有可用技能
- 按名称搜索技能
- 查找特定技能文件
- 显示技能详细信息
- 支持模糊搜索

## Code
```python
#!/usr/bin/env python3
"""
Find Skills Skill - 技能查找工具
用于搜索和管理已安装的技能
"""

import os
import re
import json
import sys
import argparse
from pathlib import Path

def find_skill_files(skills_dir="skills"):
    """查找技能目录中的所有文件"""
    skills_path = Path(skills_dir)
    if not skills_path.exists():
        return []
    
    skill_files = []
    for file_path in skills_path.rglob("*"):
        if file_path.is_file():
            skill_files.append(str(file_path))
    
    return skill_files

def list_skills(skills_dir="skills"):
    """列出所有技能"""
    skill_files = find_skill_files(skills_dir)
    skills = {}
    
    for file_path in skill_files:
        path = Path(file_path)
        skill_name = path.stem
        
        if skill_name not in skills:
            skills[skill_name] = {
                'name': skill_name,
                'files': [],
                'description': '',
                'usage': ''
            }
        
        skills[skill_name]['files'].append(file_path)
        
        # 如果是.md文件，尝试提取描述和使用方法
        if path.suffix == '.md':
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    # 提取描述
                    desc_match = re.search(r'## Description\s*\n(.*?)(?=\n##|\n#|$)', content, re.DOTALL)
                    if desc_match:
                        skills[skill_name]['description'] = desc_match.group(1).strip()
                    
                    # 提取使用方法
                    usage_match = re.search(r'## Usage\s*\n(.*?)(?=\n##|\n#|$)', content, re.DOTALL)
                    if usage_match:
                        skills[skill_name]['usage'] = usage_match.group(1).strip()
            except Exception as e:
                pass
    
    return list(skills.values())

def search_skills(query, skills_dir="skills"):
    """搜索技能"""
    skills = list_skills(skills_dir)
    results = []
    
    query_lower = query.lower()
    for skill in skills:
        # 在名称、描述和使用方法中搜索
        if (query_lower in skill['name'].lower() or 
            query_lower in skill['description'].lower() or
            query_lower in skill['usage'].lower()):
            results.append(skill)
    
    return results

def find_skill_files_by_pattern(pattern, skills_dir="skills"):
    """按模式查找技能文件"""
    skill_files = find_skill_files(skills_dir)
    matching_files = []
    
    pattern_lower = pattern.lower()
    for file_path in skill_files:
        if pattern_lower in file_path.lower():
            matching_files.append(file_path)
    
    return matching_files

def get_skill_info(skill_name, skills_dir="skills"):
    """获取特定技能的详细信息"""
    skills = list_skills(skills_dir)
    
    for skill in skills:
        if skill['name'].lower() == skill_name.lower():
            return skill
    
    return None

def main():
    parser = argparse.ArgumentParser(description='技能查找工具')
    parser.add_argument('--list', action='store_true', help='列出所有技能')
    parser.add_argument('--search', type=str, help='搜索技能')
    parser.add_argument('--find', type=str, help='查找技能文件')
    parser.add_argument('--info', type=str, help='获取技能详细信息')
    parser.add_argument('--skills-dir', type=str, default='skills', help='技能目录路径')
    
    args = parser.parse_args()
    
    if args.list:
        skills = list_skills(args.skills_dir)
        print(json.dumps(skills, indent=2, ensure_ascii=False))
    
    elif args.search:
        results = search_skills(args.search, args.skills_dir)
        print(json.dumps(results, indent=2, ensure_ascii=False))
    
    elif args.find:
        results = find_skill_files_by_pattern(args.find, args.skills_dir)
        print(json.dumps(results, indent=2, ensure_ascii=False))
    
    elif args.info:
        skill_info = get_skill_info(args.info, args.skills_dir)
        if skill_info:
            print(json.dumps(skill_info, indent=2, ensure_ascii=False))
        else:
            print(json.dumps({'error': f'Skill "{args.info}" not found'}, indent=2))
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
```