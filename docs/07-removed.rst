#######
 删除的功能
#######

*********************
 删除 ``paddle`` 模式的支持
*********************

``paddlepaddle-tiny`` 已停更， 仅支持 Python ≤3.6 现代 Python（3.8+）必须装完整 ``paddle``
，体积大、安装易报错

- 精度：不如现代 PaddleNLP、LLM 分词、BERT/ERNIE 小模型
- 速度：远慢于默认模式
- 社区：极少项目生产环境用 paddle 模式

LAC (Lexical Analysis of Chinese) 是百度开源的中文词法分析工具， 基于深度学习框架 ``PaddlePaddle`` 实现。

``lac_small`` 在 ``jieba`` 中的用途

``lac_small`` 是 ``jieba`` 的 ``paddle`` 模式的核心组件， 用于提供基于深度学习的分词和词性标注功能。

**********
 生成的文件的维护
**********

原代码库为什么会有 ``.p`` 和 ``.py`` 两种文件？ 这是为了兼容性和性能做的权衡：

- ``.p`` 文件 (Pickle)：这是 Python 的二进制序列化格式。 用途：主要用于 Jython（运行在 Java 虚拟机上的 Python）。
- ``.py`` 文件 (Python 源码)：这些文件里通常只有一行： ``P = {...}`` ，把数据存成了一个巨大的字典常量。 用途：用于标准的
  CPython。 Python 解释器对加载编译好的 ``.pyc`` 字节码优化得很好， 直接导入模块比解析 Pickle
  文件在某些环境下更安全、启动更快， 且不容易出现版本兼容问题。

两个文件夹之间的重复（finalseg vs posseg）

``finalseg`` 和 ``posseg`` 里都有 ``prob_start.py`` 等文件，这是因为：

- ``finalseg`` ：负责分词（判断一个字是 B/M/E/S）。
- ``posseg`` ：负责词性标注（判断一个词是 n/v/adj 等）。

它们底层都使用了 HMM（隐马尔可夫模型）， 所以都需要“初始概率 (start)”、“转移概率 (trans)”和“发射概率 (emit)”。
注意：虽然文件名一样，但里面的数据是不一样的！ ``posseg`` 的状态空间（States）比 ``finalseg`` 复杂得多，
所以它们的概率矩阵维度不同，不能混用。

重构这个项目，进行以下改进： 项目明确不支持 Jython（现在的 Python 项目很少支持 Jython 了）， 可以删除所有的 ``.p`` 文件。 简化
``__init__.py`` 中的加载逻辑， 只保留 ``from .prob_start import P`` 。 这样能显著减少包的大小和复杂度。
