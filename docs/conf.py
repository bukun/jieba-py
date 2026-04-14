# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
from pathlib import Path

# 添加项目根目录到路径，以便读取 pyproject.toml
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    import tomllib
except ImportError:
    # Python < 3.11 兼容性
    import tomli as tomllib

# 读取 pyproject.toml 获取版本号
pyproject_path = Path(__file__).parent.parent / 'pyproject.toml'
with open(pyproject_path, 'rb') as f:
    pyproject_data = tomllib.load(f)

project_version = pyproject_data['project']['version']

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'jieba-py'
copyright = '2026, bukun'
author = 'bukun'
release = project_version
version = project_version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

root_doc = 'index'
language = 'zh'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# 添加自定义 CSS
html_css_files = [
    'custom.css',
]

# 不复制源文件到输出目录
html_copy_source = False
html_show_sourcelink = False