#!/usr/bin/env python3
import subprocess
import json

# 测试技能查找工具
result = subprocess.run(['python3', 'find_skills.py', '--list'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print("技能查找工具测试结果:")
print("返回码:", result.returncode)
print("输出:", result.stdout.decode('utf-8'))
print("错误:", result.stderr.decode('utf-8'))