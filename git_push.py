#!/usr/bin/env python3
import subprocess
import sys

# 执行git push
result = subprocess.run(['git', 'push', 'origin', 'main'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
print("Git push 结果:")
print("返回码:", result.returncode)
print("输出:", result.stdout)
if result.stderr:
    print("错误:", result.stderr)