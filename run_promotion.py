#!/usr/bin/env python3
import subprocess
import sys

# 运行营销推广工具
result = subprocess.run([sys.executable, 'promotion_tool.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
print("营销推广工具运行结果:")
print("返回码:", result.returncode)
print("输出:", result.stdout)
if result.stderr:
    print("错误:", result.stderr)