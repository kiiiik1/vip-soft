#!/bin/bash

# 开发者工具包安装脚本
# 自动安装和配置批量重命名工具和代码质量检查工具

set -e

echo "🚀 开发者工具包安装脚本"
echo "=========================="

# 检查Python版本
check_python() {
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
        PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d'.' -f1)
        PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d'.' -f2)
        
        if [ "$PYTHON_MAJOR" -ge 3 ] && [ "$PYTHON_MINOR" -ge 6 ]; then
            echo "✅ Python版本检查通过: $PYTHON_VERSION"
            PYTHON_CMD="python3"
            return 0
        else
            echo "❌ Python版本过低，需要3.6或更高版本"
            return 1
        fi
    else
        echo "❌ 未找到Python3，请先安装Python 3.6或更高版本"
        return 1
    fi
}

# 检查pip
check_pip() {
    if command -v pip3 &> /dev/null; then
        echo "✅ pip3已安装"
        PIP_CMD="pip3"
        return 0
    elif command -v pip &> /dev/null; then
        echo "✅ pip已安装"
        PIP_CMD="pip"
        return 0
    else
        echo "❌ 未找到pip，请先安装pip"
        return 1
    fi
}

# 安装依赖
install_dependencies() {
    echo "📦 安装Python依赖..."
    
    # 升级pip
    $PIP_CMD install --upgrade pip
    
    # 安装依赖
    $PIP_CMD install -r requirements.txt
    
    if [ $? -eq 0 ]; then
        echo "✅ 依赖安装成功"
        return 0
    else
        echo "❌ 依赖安装失败"
        return 1
    fi
}

# 运行测试
run_tests() {
    echo "🧪 运行测试..."
    $PYTHON_CMD test_runner.py
    
    if [ $? -eq 0 ]; then
        echo "✅ 测试通过"
        return 0
    else
        echo "❌ 测试失败"
        return 1
    fi
}

# 创建可执行脚本
create_executables() {
    echo "🔧 创建可执行脚本..."
    
    # 创建批量重命名工具脚本
    cat > batch_rename << 'EOF'
#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "$SCRIPT_DIR/batch_renamer.py" "$@"
EOF
    
    # 创建代码质量检查工具脚本
    cat > code_check << 'EOF'
#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "$SCRIPT_DIR/code_quality_checker.py" "$@"
EOF
    
    # 创建演示工具脚本
    cat > demo << 'EOF'
#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "$SCRIPT_DIR/demo_tools.py" "$@"
EOF
    
    # 设置执行权限
    chmod +x batch_rename code_check demo
    
    echo "✅ 可执行脚本创建成功"
    echo "   - batch_rename: 批量重命名工具"
    echo "   - code_check: 代码质量检查工具"
    echo "   - demo: 演示工具"
}

# 添加到PATH（可选）
add_to_path() {
    read -p "是否要将工具添加到系统PATH？[y/N]: " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        # 获取当前用户的主目录
        HOME_DIR=$(eval echo ~$USER)
        
        # 创建bin目录（如果不存在）
        BIN_DIR="$HOME_DIR/bin"
        mkdir -p "$BIN_DIR"
        
        # 创建符号链接
        ln -sf "$(pwd)/batch_rename" "$BIN_DIR/batch_rename"
        ln -sf "$(pwd)/code_check" "$BIN_DIR/code_check"
        ln -sf "$(pwd)/demo" "$BIN_DIR/demo"
        
        # 检查是否已经在PATH中
        if [[ ":$PATH:" != *":$BIN_DIR:"* ]]; then
            echo "export PATH=\"\$PATH:$BIN_DIR\"" >> "$HOME_DIR/.bashrc"
            echo "✅ 已添加到PATH，请重新加载终端或运行: source ~/.bashrc"
        else
            echo "✅ 工具已在PATH中"
        fi
    fi
}

# 显示安装完成信息
show_completion() {
    echo ""
    echo "🎉 安装完成！"
    echo "=========================="
    echo ""
    echo "📋 使用方法："
    echo "   批量重命名: ./batch_rename --help"
    echo "   代码质量检查: ./code_check --help"
    echo "   运行演示: ./demo"
    echo ""
    echo "📖 更多信息请查看："
    echo "   - README.md: 项目介绍"
    echo "   - USAGE.md: 使用指南"
    echo "   - LICENSE: 许可证信息"
    echo ""
    echo "🔧 快速测试："
    echo "   ./demo"
    echo ""
    echo "📞 技术支持："
    echo "   - GitHub: https://github.com/your-username/developer-tools-bundle"
    echo "   - 邮箱: support@example.com"
    echo ""
}

# 主安装流程
main() {
    echo "开始安装..."
    
    # 检查依赖
    check_python || exit 1
    check_pip || exit 1
    
    # 安装依赖
    install_dependencies || exit 1
    
    # 运行测试
    run_tests || exit 1
    
    # 创建可执行脚本
    create_executables
    
    # 添加到PATH（可选）
    add_to_path
    
    # 显示完成信息
    show_completion
}

# 运行主函数
main "$@"