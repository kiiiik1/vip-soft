#!/usr/bin/env python3
"""
VIP Soft 工具测试套件
测试所有核心工具的功能
"""

import json
import os
import sys
import subprocess
import time
from pathlib import Path

def test_search_tool():
    """测试搜索工具"""
    print("🔍 测试搜索工具...")
    
    try:
        # 测试基本搜索功能
        result = subprocess.run([
            sys.executable, 'search.py', 'test search'
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=30)
        
        if result.returncode == 0:
            search_results = json.loads(result.stdout)
            if isinstance(search_results, list) and len(search_results) > 0:
                print("✅ 搜索工具测试通过")
                return True
            else:
                print("❌ 搜索工具返回结果格式错误")
                return False
        else:
            print(f"❌ 搜索工具测试失败: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ 搜索工具测试异常: {str(e)}")
        return False

def test_skills_tool():
    """测试技能查找工具"""
    print("🛠️ 测试技能查找工具...")
    
    try:
        # 测试列出技能功能
        result = subprocess.run([
            sys.executable, 'find_skills.py', '--list'
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=10)
        
        if result.returncode == 0:
            skills_data = json.loads(result.stdout)
            if isinstance(skills_data, list):
                print("✅ 技能查找工具测试通过")
                return True
            else:
                print("❌ 技能查找工具返回结果格式错误")
                return False
        else:
            print(f"❌ 技能查找工具测试失败: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ 技能查找工具测试异常: {str(e)}")
        return False

def test_install_script():
    """测试安装脚本（仅检查语法）"""
    print("⚙️ 测试安装脚本...")
    
    try:
        # 检查bash脚本语法
        result = subprocess.run([
            'bash', '-n', 'install.sh'
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode == 0:
            print("✅ 安装脚本语法检查通过")
            return True
        else:
            print(f"❌ 安装脚本语法错误: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ 安装脚本测试异常: {str(e)}")
        return False

def run_all_tests():
    """运行所有测试"""
    print("🧪 VIP Soft 工具测试套件")
    print("=" * 40)
    
    tests = [
        test_search_tool,
        test_skills_tool,
        test_install_script
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 40)
    print(f"测试结果: {passed}/{total} 通过")
    
    if passed == total:
        print("🎉 所有测试通过！")
        return True
    else:
        print("⚠️ 部分测试失败，请检查工具功能")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)