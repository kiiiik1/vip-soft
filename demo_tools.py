#!/usr/bin/env python3
"""
开发者工具包演示脚本
展示批量重命名工具和代码质量检查工具的功能
"""

import os
import sys
import subprocess
import tempfile
import shutil
from pathlib import Path

def create_demo_files():
    """创建演示用的测试文件"""
    demo_dir = Path("demo_files")
    demo_dir.mkdir(exist_ok=True)
    
    # 创建一些测试文件
    test_files = [
        "IMG_1234.jpg",
        "IMG_1235.jpg", 
        "IMG_1236.jpg",
        "document_v1.txt",
        "document_v2.txt",
        "code.py",
        "script.js"
    ]
    
    for filename in test_files:
        filepath = demo_dir / filename
        with open(filepath, 'w') as f:
            if filename.endswith('.py'):
                f.write("# Python demo file\nprint('Hello World')\n")
            elif filename.endswith('.js'):
                f.write("// JavaScript demo file\nconsole.log('Hello World');\n")
            else:
                f.write(f"Demo content for {filename}\n")
    
    return demo_dir

def demo_batch_rename():
    """演示批量重命名功能"""
    print("=== 批量重命名工具演示 ===")
    
    # 创建测试文件
    demo_dir = create_demo_files()
    os.chdir(demo_dir)
    
    print("原始文件列表:")
    for file in os.listdir('.'):
        print(f"  {file}")
    
    # 模拟批量重命名功能
    print("\n执行批量重命名...")
    
    # 1. 序号重命名
    print("1. 序号重命名:")
    index = 1
    for file in os.listdir('.'):
        if file.endswith(('.jpg', '.txt', '.py', '.js')):
            new_name = f"{index:03d}_{file}"
            print(f"  {file} -> {new_name}")
            index += 1
    
    # 2. 字符串替换
    print("\n2. 字符串替换:")
    for file in os.listdir('.'):
        if 'IMG_' in file:
            new_name = file.replace('IMG_', 'PHOTO_')
            print(f"  {file} -> {new_name}")
    
    # 3. 日期重命名
    print("\n3. 日期重命名:")
    from datetime import datetime
    date_str = datetime.now().strftime("%Y-%m-%d")
    for file in os.listdir('.'):
        if file.endswith(('.jpg', '.txt')):
            new_name = f"{date_str}_{file}"
            print(f"  {file} -> {new_name}")
    
    # 清理
    os.chdir('..')
    shutil.rmtree(demo_dir)
    
    print("\n批量重命名演示完成!")

def demo_code_quality():
    """演示代码质量检查功能"""
    print("\n=== 代码质量检查工具演示 ===")
    
    # 创建测试代码文件
    demo_dir = Path("code_demo")
    demo_dir.mkdir(exist_ok=True)
    
    # 创建一些有问题的代码文件
    problematic_py = demo_dir / "problematic.py"
    with open(problematic_py, 'w') as f:
        f.write("""
# 过长的行，超过建议长度
this_is_a_very_long_line_that_exceeds_the_recommended_length_for_python_code_standards = "value"

import os
import sys
import json  # 未使用的导入
import re

def complex_function():
    # TODO: 需要重构这个复杂函数
    if condition1 and condition2 and condition3 and condition4 and condition5:
        if nested_condition1 or nested_condition2:
            for item in long_list:
                if item.check():
                    return True
    return False
""")

    good_py = demo_dir / "good_example.py"
    with open(good_py, 'w') as f:
        f.write("""# 规范的代码示例
import os
import sys

def simple_function():
    # 简单的函数示例
    if condition1:
        return True
    return False
""")

    print("检查文件:")
    for file in demo_dir.glob("*.py"):
        print(f"  {file.name}")
    
    print("\n代码质量检查结果:")
    
    # 模拟代码检查
    for file in demo_dir.glob("*.py"):
        print(f"\n{file.name}:")
        
        with open(file, 'r') as f:
            lines = f.readlines()
        
        line_number = 0
        for line in lines:
            line_number += 1
            
            # 检查行长度
            if len(line.strip()) > 80:
                print(f"  第{line_number}行: 行过长 ({len(line.strip())} 字符)")
            
            # 检查TODO
            if 'TODO' in line:
                print(f"  第{line_number}行: 发现TODO注释")
            
            # 检查复杂条件
            if ' and ' in line or ' or ' in line:
                conditions = line.count(' and ') + line.count(' or ')
                if conditions > 2:
                    print(f"  第{line_number}行: 复杂条件语句 (包含 {conditions} 个条件)")
            
            # 检查未使用的导入
            if line.strip().startswith('import ') and 'import os' in line:
                print(f"  第{line_number}行: 可能未使用的导入")

    # 清理
    shutil.rmtree(demo_dir)
    
    print("\n代码质量检查演示完成!")

def main():
    """主演示函数"""
    print("🚀 开发者工具包功能演示")
    print("=" * 50)
    
    demo_batch_rename()
    demo_code_quality()
    
    print("\n" + "=" * 50)
    print("演示完成!")
    print("\n立即购买完整版本:")
    print("- 个人版: $4.99")
    print("- 专业版: $9.99") 
    print("- 企业版: $19.99")
    print("\n通过支付宝扫码支付或联系邮箱获取激活码")

if __name__ == '__main__':
    main()