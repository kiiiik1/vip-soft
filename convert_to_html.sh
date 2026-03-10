#!/bin/bash

# OpenClaw & ZeroClaw Money Making Guide Simple HTML Converter
# 简单的HTML转换器，不依赖Python库

echo "🚀 开始转换Markdown文件为HTML..."

# 创建输出目录
mkdir -p html-output

# 简单的HTML模板函数
create_html_template() {
    local title="$1"
    local content="$2"
    local output_file="$3"
    
    cat > "$output_file" << EOF
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>$title</title>
    <style>
        body {
            font-family: 'Arial', 'Microsoft YaHei', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
            background-color: #f9f9f9;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 15px;
            margin-bottom: 30px;
        }
        h2 {
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 8px;
            margin-top: 30px;
        }
        h3 {
            color: #2c3e50;
            border-bottom: 1px solid #3498db;
            padding-bottom: 5px;
            margin-top: 25px;
        }
        ul, ol {
            margin: 15px 0;
            padding-left: 25px;
        }
        li {
            margin: 8px 0;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }
        pre {
            background-color: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            margin: 15px 0;
            border-left: 4px solid #3498db;
        }
        blockquote {
            border-left: 4px solid #3498db;
            margin: 15px 0;
            padding-left: 15px;
            color: #666;
            font-style: italic;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
            font-weight: bold;
        }
        .price {
            background-color: #e8f5e8;
            padding: 15px;
            border-radius: 5px;
            margin: 15px 0;
            border-left: 4px solid #27ae60;
        }
        .warning {
            background-color: #fff3cd;
            padding: 15px;
            border-radius: 5px;
            margin: 15px 0;
            border-left: 4px solid #ffc107;
        }
        .success {
            background-color: #d4edda;
            padding: 15px;
            border-radius: 5px;
            margin: 15px 0;
            border-left: 4px solid #28a745;
        }
        .toc {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 5px;
            margin: 20px 0;
            border-left: 4px solid #6c757d;
        }
        .toc ul {
            list-style-type: none;
            padding-left: 0;
        }
        .toc a {
            text-decoration: none;
            color: #3498db;
        }
        .toc a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        $content
    </div>
</body>
</html>
EOF
}

# 转换Markdown为HTML的简单函数
convert_md_to_html() {
    local md_file="$1"
    local html_file="$2"
    local title="$3"
    
    # 读取Markdown文件
    if [ ! -f "$md_file" ]; then
        echo "❌ 文件不存在: $md_file"
        return 1
    fi
    
    # 读取文件内容
    local content=$(cat "$md_file")
    
    # 简单的Markdown到HTML转换
    # 标题
    content=$(echo "$content" | sed 's/^# \(.*\)$/\<h1\>\1\<\/h1\>/g')
    content=$(echo "$content" | sed 's/^## \(.*\)$/\<h2\>\1\<\/h2\>/g')
    content=$(echo "$content" | sed 's/^### \(.*\)$/\<h3\>\1\<\/h3\>/g')
    content=$(echo "$content" | sed 's/^#### \(.*\)$/\<h4\>\1\<\/h4\>/g')
    
    # 列表
    content=$(echo "$content" | sed 's/^\* \(.*\)$/\<li\>\1\<\/li\>/g')
    content=$(echo "$content" | sed 's/^\+ \(.*\)$/\<li\>\1\<\/li\>/g')
    content=$(echo "$content" | sed 's/^- \(.*\)$/\<li\>\1\<\/li\>/g')
    
    # 代码块
    content=$(echo "$content" | sed 's/```/\<pre\><code\>/g')
    content=$(echo "$content" | sed 's/^```$/\<\/code\>\<\/pre\>/g')
    
    # 行内代码
    content=$(echo "$content" | sed 's/`\([^`]*\)`/\<code\>\1\<\/code\>/g')
    
    # 引用
    content=$(echo "$content" | sed 's/^> \(.*\)$/\<blockquote\>\1\<\/blockquote\>/g')
    
    # 链接
    content=$(echo "$content" | sed 's/\[\(.*\)\](\(.*\))/\<a href="\2"\>\1\<\/a\>/g')
    
    # 分割线
    content=$(echo "$content" | sed 's/^---$/\<hr\>/g')
    
    # 段落
    content=$(echo "$content" | sed 's/^$/\<p\>\<\/p\>/g')
    
    # 创建HTML模板
    create_html_template "$title" "$content" "$html_file"
    
    echo "✅ 成功转换: $md_file -> $html_file"
    return 0
}

# 转换文件
convert_md_to_html "zeroclaw-money-guide/OpenClaw_ZeroClaw_Money_Making_Secrets_EN.md" \
                   "html-output/OpenClaw_ZeroClaw_Money_Making_Secrets_EN.html" \
                   "OpenClaw & ZeroClaw Money Making Secrets"

convert_md_to_html "zeroclaw-money-guide/OpenClaw_ZeroClaw_Money_Making_Secrets_CN.md" \
                   "html-output/OpenClaw_ZeroClaw_Money_Making_Secrets_CN.html" \
                   "OpenClaw & ZeroClaw 赚钱秘籍"

# 创建一个简单的索引页面
cat > html-output/index.html << EOF
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>OpenClaw & ZeroClaw Money Making Guide</title>
    <style>
        body {
            font-family: 'Arial', 'Microsoft YaHei', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
            background-color: #f9f9f9;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 15px;
            margin-bottom: 30px;
        }
        .card {
            background-color: #f8f9fa;
            padding: 20px;
            margin: 20px 0;
            border-radius: 8px;
            border-left: 4px solid #3498db;
        }
        .card h2 {
            margin-top: 0;
            color: #2c3e50;
        }
        .card p {
            margin-bottom: 15px;
        }
        .price {
            background-color: #e8f5e8;
            padding: 15px;
            border-radius: 5px;
            margin: 15px 0;
            border-left: 4px solid #27ae60;
        }
        .btn {
            display: inline-block;
            background-color: #3498db;
            color: white;
            padding: 12px 24px;
            text-decoration: none;
            border-radius: 5px;
            margin: 10px 5px;
        }
        .btn:hover {
            background-color: #2980b9;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 OpenClaw & ZeroClaw Money Making Guide</h1>
        
        <div class="card">
            <h2>💰 赚钱秘籍</h2>
            <p>完整的 OpenClaw & ZeroClaw 赚钱指南，包含中英双语版本。</p>
            
            <div class="price">
                <h3>🎯 定价策略</h3>
                <p><strong>基础版:</strong> $29 - 基本概念和策略</p>
                <p><strong>专业版:</strong> $97 - 详细实施指南和案例研究</p>
                <p><strong>企业版:</strong> $297 - 完整解决方案和定制咨询</p>
            </div>
            
            <h3>📚 内容预览</h3>
            <p>• 核心盈利策略</p>
            <p>• 实施路线图</p>
            <p>• 盈利模式</p>
            <p>• 案例分析</p>
            <p>• 技术设置</p>
            <p>• 营销与销售</p>
            <p>• 法律考虑</p>
            <p>• 未来趋势</p>
        </div>
        
        <div class="card">
            <h2>🌐 下载链接</h2>
            <a href="OpenClaw_ZeroClaw_Money_Making_Secrets_EN.html" class="btn">📄 English Version</a>
            <a href="OpenClaw_ZeroClaw_Money_Making_Secrets_CN.html" class="btn">📄 中文版本</a>
        </div>
        
        <div class="card">
            <h2>🎯 销售渠道</h2>
            <p><strong>自有网站:</strong> 建立专业的销售网站</p>
            <p><strong>第三方平台:</strong> Gumroad, Teachable, Kajabi</p>
            <p><strong>直接销售:</strong> 邮件营销，社交媒体</p>
        </div>
        
        <div class="card">
            <h2>📞 联系方式</h2>
            <p><strong>邮箱:</strong> support@zeroclaw-money.com</p>
            <p><strong>网站:</strong> www.zeroclaw-money.com</p>
            <p><strong>LinkedIn:</strong> linkedin.com/company/zeroclaw-money</p>
        </div>
    </div>
</body>
</html>
EOF

echo ""
echo "📊 转换完成！"
echo "📁 HTML文件保存在: $(pwd)/html-output"
echo "🌐 打开 index.html 查看预览"