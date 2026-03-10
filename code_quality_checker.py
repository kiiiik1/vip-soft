#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
代码质量检查工具
支持Python、JavaScript、Java等多种语言
"""

import os
import re
import argparse
import json
from datetime import datetime
import subprocess

class CodeQualityChecker:
    def __init__(self, directory=".", output_format="json"):
        self.directory = directory
        self.output_format = output_format
        self.results = {
            "timestamp": datetime.now().isoformat(),
            "directory": directory,
            "summary": {},
            "files": []
        }
        
    def scan_files(self, extensions=None):
        """扫描目录中的代码文件"""
        if extensions is None:
            extensions = ['.py', '.js', '.java', '.cpp', '.c', '.h', '.hpp']
        
        for root, dirs, files in os.walk(self.directory):
            # 跳过隐藏目录和特定目录
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', '__pycache__', 'venv']]
            
            for file in files:
                if any(file.endswith(ext) for ext in extensions):
                    file_path = os.path.join(root, file)
                    self.check_file(file_path)
        
        self.generate_summary()
    
    def check_file(self, file_path):
        """检查单个文件的代码质量"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            file_result = {
                "path": file_path,
                "size": len(content),
                "issues": [],
                "metrics": {}
            }
            
            # 基础指标
            file_result["metrics"]["lines"] = len(content.split('\n'))
            file_result["metrics"]["empty_lines"] = len([line for line in content.split('\n') if not line.strip()])
            file_result["metrics"]["comments"] = len(re.findall(r'#.*|//.*|/\*.*\*/', content, re.MULTILINE))
            
            # 检查常见问题
            issues = self.check_common_issues(content, file_path)
            file_result["issues"] = issues
            
            self.results["files"].append(file_result)
            
        except Exception as e:
            print(f"检查文件 {file_path} 时出错: {e}")
    
    def check_common_issues(self, content, file_path):
        """检查常见的代码质量问题"""
        issues = []
        
        # 检查行长度
        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            if len(line) > 120:
                issues.append({
                    "type": "line_too_long",
                    "line": i,
                    "message": f"第{i}行过长 ({len(line)} 字符)",
                    "severity": "warning"
                })
        
        # 检查TODO注释
        todos = re.finditer(r'TODO|FIXME|HACK', content, re.IGNORECASE)
        for match in todos:
            line_num = content[:match.start()].count('\n') + 1
            issues.append({
                "type": "todo_comment",
                "line": line_num,
                "message": f"发现TODO注释: {match.group()}",
                "severity": "info"
            })
        
        # 检查未使用的导入（Python）
        if file_path.endswith('.py'):
            unused_imports = self.check_unused_imports(content)
            for imp in unused_imports:
                issues.append({
                    "type": "unused_import",
                    "line": imp['line'],
                    "message": f"未使用的导入: {imp['name']}",
                    "severity": "warning"
                })
        
        # 检查复杂的条件语句
        complex_conditions = re.finditer(r'if\s+.*&&.*&&', content, re.IGNORECASE)
        for match in complex_conditions:
            line_num = content[:match.start()].count('\n') + 1
            issues.append({
                "type": "complex_condition",
                "line": line_num,
                "message": "复杂的条件语句，建议拆分",
                "severity": "warning"
            })
        
        return issues
    
    def check_unused_imports(self, content):
        """检查Python文件中未使用的导入"""
        issues = []
        imports = re.finditer(r'^\s*import\s+([\w.]+)|^\s*from\s+([\w.]+)\s+import', content, re.MULTILINE)
        
        for match in imports:
            import_name = match.group(1) or match.group(2)
            # 简单检查：如果导入的名称没有在代码中使用，可能未使用
            if import_name and import_name not in content[match.end():]:
                issues.append({
                    'name': import_name,
                    'line': content[:match.start()].count('\n') + 1
                })
        
        return issues
    
    def generate_summary(self):
        """生成检查摘要"""
        total_files = len(self.results["files"])
        total_issues = sum(len(f["issues"]) for f in self.results["files"])
        
        self.results["summary"] = {
            "total_files": total_files,
            "total_issues": total_issues,
            "issues_by_type": {},
            "average_file_size": sum(f["size"] for f in self.results["files"]) / total_files if total_files > 0 else 0
        }
        
        # 统计问题类型
        for file_result in self.results["files"]:
            for issue in file_result["issues"]:
                issue_type = issue["type"]
                if issue_type not in self.results["summary"]["issues_by_type"]:
                    self.results["summary"]["issues_by_type"][issue_type] = 0
                self.results["summary"]["issues_by_type"][issue_type] += 1
    
    def generate_report(self):
        """生成报告"""
        if self.output_format == "json":
            return json.dumps(self.results, indent=2, ensure_ascii=False)
        elif self.output_format == "text":
            return self.generate_text_report()
        else:
            return str(self.results)
    
    def generate_text_report(self):
        """生成文本报告"""
        report = []
        report.append("=== 代码质量检查报告 ===")
        report.append(f"检查时间: {self.results['timestamp']}")
        report.append(f"检查目录: {self.results['directory']}")
        report.append("")
        
        # 摘要
        summary = self.results["summary"]
        report.append("=== 摘要 ===")
        report.append(f"总文件数: {summary['total_files']}")
        report.append(f"总问题数: {summary['total_issues']}")
        report.append(f"平均文件大小: {summary['average_file_size']:.2f} 字节")
        report.append("")
        
        # 问题类型统计
        report.append("=== 问题类型统计 ===")
        for issue_type, count in summary["issues_by_type"].items():
            report.append(f"{issue_type}: {count}")
        report.append("")
        
        # 详细问题
        for file_result in self.results["files"]:
            if file_result["issues"]:
                report.append(f"=== {file_result['path']} ===")
                for issue in file_result["issues"]:
                    report.append(f"第{issue['line']}行 [{issue['severity']}] {issue['message']}")
                report.append("")
        
        return "\n".join(report)

def main():
    parser = argparse.ArgumentParser(description="代码质量检查工具")
    parser.add_argument("directory", nargs="?", default=".", help="目标目录")
    parser.add_argument("--format", choices=["json", "text"], default="json", help="输出格式")
    parser.add_argument("--output", help="输出文件路径")
    
    args = parser.parse_args()
    
    checker = CodeQualityChecker(args.directory, args.format)
    checker.scan_files()
    
    report = checker.generate_report()
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"报告已保存到: {args.output}")
    else:
        print(report)

if __name__ == "__main__":
    main()