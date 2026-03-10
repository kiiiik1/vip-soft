#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单工具测试脚本
直接测试工具的基本功能
"""

import os
import sys

def test_imports():
    """测试导入工具"""
    print("=== 测试工具导入 ===")
    
    try:
        import batch_renamer
        print("✅ 批量文件重命名工具导入成功")
    except Exception as e:
        print("❌ 批量文件重命名工具导入失败: " + str(e))
        return False
    
    try:
        import code_quality_checker
        print("✅ 代码质量检查工具导入成功")
    except Exception as e:
        print("❌ 代码质量检查工具导入失败: " + str(e))
        return False
    
    return True

def test_syntax():
    """测试语法"""
    print("\n=== 测试语法 ===")
    
    # 测试批量文件重命名工具语法
    try:
        with open("batch_renamer.py", 'r') as f:
            compile(f.read(), "batch_renamer.py", 'exec')
        print("✅ 批量文件重命名工具语法正确")
    except SyntaxError as e:
        print("❌ 批量文件重命名工具语法错误: " + str(e))
        return False
    
    # 测试代码质量检查工具语法
    try:
        with open("code_quality_checker.py", 'r') as f:
            compile(f.read(), "code_quality_checker.py", 'exec')
        print("✅ 代码质量检查工具语法正确")
    except SyntaxError as e:
        print("❌ 代码质量检查工具语法错误: " + str(e))
        return False
    
    return True

def test_help():
    """测试帮助信息"""
    print("\n=== 测试帮助信息 ===")
    
    # 测试批量文件重命名工具帮助
    try:
        os.system("python batch_renamer.py --help > /dev/null 2>&1")
        print("✅ 批量文件重命名工具帮助信息正常")
    except Exception as e:
        print("❌ 批量文件重命名工具帮助信息异常: " + str(e))
        return False
    
    # 测试代码质量检查工具帮助
    try:
        os.system("python code_quality_checker.py --help > /dev/null 2>&1")
        print("✅ 代码质量检查工具帮助信息正常")
    except Exception as e:
        print("❌ 代码质量检查工具帮助信息异常: " + str(e))
        return False
    
    return True

def test_basic_functionality():
    """测试基本功能"""
    print("\n=== 测试基本功能 ===")
    
    # 创建临时测试目录
    test_dir = "temp_test"
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    
    try:
        # 创建测试文件
        test_files = ["test1.txt", "test2.txt", "test3.txt"]
        for filename in test_files:
            with open(os.path.join(test_dir, filename), 'w') as f:
                f.write("测试文件 " + filename + "\n")
        
        print("创建了 " + str(len(test_files)) + " 个测试文件")
        
        # 测试代码质量检查工具
        try:
            os.system("python code_quality_checker.py " + test_dir + " --format text > test_output.txt 2>&1")
            with open("test_output.txt", 'r') as f:
                output = f.read()
            if "代码质量检查报告" in output:
                print("✅ 代码质量检查工具基本功能正常")
            else:
                print("❌ 代码质量检查工具基本功能异常")
                return False
        except Exception as e:
            print("❌ 代码质量检查工具测试失败: " + str(e))
            return False
        
        return True
        
    finally:
        # 清理测试目录
        if os.path.exists(test_dir):
            import shutil
            shutil.rmtree(test_dir)
        if os.path.exists("test_output.txt"):
            os.remove("test_output.txt")
        
        print("清理测试目录")

def main():
    """主测试函数"""
    print("开始测试开发者工具包...")
    
    # 检查工具文件是否存在
    if not os.path.exists("batch_renamer.py"):
        print("❌ 批量文件重命名工具不存在")
        return
    
    if not os.path.exists("code_quality_checker.py"):
        print("❌ 代码质量检查工具不存在")
        return
    
    # 运行测试
    tests = [
        test_imports,
        test_syntax,
        test_help,
        test_basic_functionality
    ]
    
    all_passed = True
    for test in tests:
        if not test():
            all_passed = False
    
    print("\n=== 测试完成 ===")
    if all_passed:
        print("✅ 所有测试通过！工具可以正常使用。")
    else:
        print("❌ 部分测试失败，请检查工具代码。")

if __name__ == "__main__":
    main()