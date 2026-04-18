# jieba-py项目说明

这些年做的工作很多都涉及到中文分词，jieba分词几乎是每个项目必须安装的模块，一直工作非常稳定。
但是由于其代码库长期不再维护，一直是使用中的一个隐患，使用中做过简单的代码修改以去除一些警告。
两年前就有想对其源码进行修改更新的想法，但是由于对自然语言处理并不算了解，没法实际动手。

这次借助于AI工具，得以快速地对项目的各个模块进行了了解，发现项目还是比较简单的。
所以我 `fork` 了此模块， 实际动手做了一些修改。
合并了原来的一点工作，这中间也大量使用了AI工具。
整体工作量不算大，完成后使用了没有大的问题。目前最新版本已经发布地pipy 。

jieba分词其实被很多语言重新。其中不乏一些项目，是可以在Python中直接使用的。
这个版本是纯Python语言的继续维护，还是有一些意义的。

- 只保证能运行在 Python 3.10 以上环境，不再考虑 Python 2 的兼容性，简化了一些代码。
- 对代码进行了格式化，方便阅读。暂时不会进行较大的修改。
- 在程序结构上使用了更新的技术手段来保证工程的稳定开发。
- 单元测试进行逐步的修改。这部分不影响核心逻辑，修改影响不大。
- 打包方式进行了修改，使用了 `pyproject.toml` 配置文件， 放弃原来的 `setup.py` 配置文件。
- 发布到 `pypi` 时使用 `jieba-py` 命名。 目前与原 `jieba` 分词用法完全一样， 只需要安装 `jieba-py`
  来代替 `jieba` 。 为了保持兼容性，使用了 `jieba` 模块名，安装时会与旧版本冲突。 如果安装了 `jieba`
  模块，一定要先卸载 `jieba` 模块： `python3 -m pip install jieba` 。
- 移除了对于 `paddle` 模式的支持。 一方面，`paddle` 模式已经不再维护， 另一方面，`paddle` 模式在Python
  3.10以上版本中无法运行。

#### NOTE
目前 `jieba-py` 模块已经发布到 `pypi` 上，请使用 `pip` 安装。最新版本为： 0.46.10

`python3 -m pip install jieba-py`



# jieba-py Project Description

Much of the work I have done over the years has involved Chinese word segmentation. Jieba is a module that must be installed for almost every project and has always worked very stably. However, since its codebase has not been maintained for a long time, it has been a hidden concern. I have made simple code modifications to remove some warnings. Two years ago, I thought about modifying and updating its source code, but I couldn’t actually do it because I didn’t know enough about natural language processing.

With the help of AI tools this time, I was able to quickly understand the various modules of the project and found that it was relatively simple. So I `forked` this module and actually made some modifications. I merged some previous work, using AI tools extensively in the process. The overall workload was not large, and there were no major issues after completion. The latest version has now been released to PyPI.

Jieba segmentation has actually been re-implemented in many languages. There are many projects among them that can be used directly in Python. This version’s continued maintenance in pure Python still has some significance.

- It is only guaranteed to run in environments with Python 3.10 or above. Python 2 compatibility is no longer considered, and some code has been simplified.
- The code has been formatted for easier reading. No major changes will be made for the time being.
- Updated technical means have been used in the program structure to ensure the stable development of the project.
- Unit tests are being gradually modified. This part does not affect the core logic, and the impact of these modifications is minor.
- The packaging method has been modified to use the `pyproject.toml` configuration file, abandoning the original `setup.py` configuration file.
- When published to `pypi`, it uses the name `jieba-py`. Currently, the usage is exactly the same as the original `jieba`. You only need to install `jieba-py` to replace `jieba`. To maintain compatibility, the `jieba` module name is used, which will conflict with the old version during installation. If the `jieba` module is installed, be sure to uninstall it first: `python3 -m pip uninstall jieba`.
- Support for `paddle` mode has been removed. On one hand, `paddle` mode is no longer maintained. On the other hand, `paddle` mode cannot run in Python versions 3.10 and above.

#### NOTE
The `jieba-py` module has been published on `pypi`. Please use `pip` to install. The latest version is: 0.46.10

`python3 -m pip install jieba-py`
