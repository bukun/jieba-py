#!/usr/bin/env python3
"""
与Jieba-py无关的辅助脚本。
"""

import re
from pathlib import Path


def sync_version(root_dir: str = '.') -> bool:
    """
    版本号同步脚本
    将 jieba_py/__init__.py 中的版本号与 pyproject.toml 保持一致
    以 pyproject.toml 的版本号为准

    Args:
        root_dir: 项目根目录

    Returns:
        True if version was synced, False if already in sync or error
    """
    root = Path(root_dir).resolve()

    # 文件路径
    pyproject_file = root / 'pyproject.toml'
    init_file = root / 'jieba' / '__init__.py'

    # 检查文件是否存在
    if not pyproject_file.exists():
        print(f'❌ 错误: 找不到 {pyproject_file}')
        return False

    if not init_file.exists():
        print(f'❌ 错误: 找不到 {init_file}')
        return False

    # 读取 pyproject.toml 版本
    pyproject_content = pyproject_file.read_text(encoding='utf-8')
    toml_match = re.search(r'version\s*=\s*"([^"]+)"', pyproject_content)

    if not toml_match:
        print('❌ 错误: 未在 pyproject.toml 中找到版本号')
        return False

    version_toml = toml_match.group(1)

    # 读取 __init__.py 版本
    init_content = init_file.read_text(encoding='utf-8')
    init_match = re.search(r"__version__\s*=\s*'([^']+)'", init_content)

    if not init_match:
        print('❌ 错误: 未在 __init__.py 中找到版本号')
        return False

    version_init = init_match.group(1)

    # 比较版本号
    if version_toml == version_init:
        print(f'✅ 版本号已一致: {version_toml}')
        return False

    # 不同步，需要更新
    print('📝 检测到版本号不一致:')
    print(f'   pyproject.toml: {version_toml}')
    print(f'   __init__.py:    {version_init}')
    print(f'🔄 正在同步 __init__.py 版本号为: {version_toml}')

    # 替换版本号
    new_init_content = re.sub(r"(__version__\s*=\s*)'[^']+'", f"\\1'{version_toml}'", init_content)

    # 写回文件
    init_file.write_text(new_init_content, encoding='utf-8')

    print('✅ 版本号同步成功!')
    print(f'   __init__.py 已更新为: {version_toml}')

    return True


if __name__ == '__main__':
    import sys

    try:
        synced = sync_version()
        sys.exit(0)
    except Exception as e:
        print(f'❌ 同步失败: {e}')
        import traceback

        traceback.print_exc()
        sys.exit(1)
