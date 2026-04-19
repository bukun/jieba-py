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

language = 'zh_CN'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [  'sphinxcontrib.programoutput',  "myst_parser",]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

root_doc = 'index'
language = 'zh_CN'

# ===================== 修复 Sphinx 9.x 中文搜索 ChineseStemmer 缺失BUG =====================
html_search_language = 'zh'

def setup(app):
    app.add_js_file(None, body="""
        // 提前定义完整的 ChineseStemmer，和官方英文Stemmer逻辑一致
        window.ChineseStemmer = function() {};
        window.ChineseStemmer.prototype.stemWord = function(word) {
            // 中文不做词干提取，直接返回原词
            return word;
        };
        window.ChineseStemmer.prototype.stem = function(word) {
            return word;
        };
        window.ChineseStemmer.prototype.addWord = function() {};
    """)
# ========================================================================================

locale_dirs = ['locale/']   # 翻译文件存放目录
gettext_compact = False     # 为每个源文件生成独立的 po 文件

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
html_logo = '_static/jieba_logo_enhanced.svg'

# 添加自定义 CSS
html_css_files = [
    'custom.css',
]

# 不复制源文件到输出目录
html_copy_source = False
html_show_sourcelink = False

suppress_warnings = [
    'ref.ref',           # 可选：忽略引用警告
    'toc.tree',          # 可选：忽略目录警告
    'docs.title',        # 忽略标题下划线/上划线太短警告
]