##############
 jieba-py项目说明
##############

在项目中使用了 ``Jieba`` 分词。由于此模块很长时间不更新，所以我 ``fork`` 了此模块， 并做了一些修改。

- 只保证能运行在 Python 3.10 以上环境，不再考虑 Python 2 的兼容性，简化了一些代码。
- 对代码进行了格式化，方便阅读。暂时不会进行较大的修改。
- 在程序结构上使用了更新的技术手段来保证工程的稳定开发。
- 单元测试进行逐步的修改。这部分不影响核心逻辑，修改影响不大。
- 打包方式进行了修改，使用了 ``pyproject.toml`` 配置文件， 放弃原来的 ``setup.py`` 配置文件。
- 发布到 ``pypi`` 时使用 ``jieba-py`` 命名。 目前与原 ``jieba`` 分词用法完全一样， 只需要安装 ``jieba-py``
  来代替 ``jieba`` 。 为了保持兼容性，使用了 ``jieba`` 模块名，安装时会与旧版本冲突。 如果安装了 ``jieba``
  模块，一定要先卸载 ``jieba`` 模块： ``python3 -m pip install jieba`` 。
- 移除了对于 ``paddle`` 模式的支持。 一方面，\ ``paddle`` 模式已经不再维护， 另一方面，\ ``paddle`` 模式在Python
  3.10以上版本中无法运行。

.. note::

    目前 ``jieba-py`` 模块已经发布到 ``pypi`` 上，请使用 ``pip`` 安装。最新版本为： |version|

    ``python3 -m pip install jieba-py``

.. toctree::
    :maxdepth: 2
    :caption: 文档目录
    :numbered: 2

    01-intro.rst
    02-usage.rst
    04-data.rst
    07-removed.rst
    08-append.rst
    09-old.rst
