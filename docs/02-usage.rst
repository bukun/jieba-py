#########
 主要功能与用法
#########

****
 分词
****

- ``jieba.cut`` 方法接受四个输入参数: 需要分词的字符串； ``cut_all`` 参数用来控制是否采用全模式；HMM 参数用来控制是否使用
  HMM 模型；
- ``jieba.cut_for_search`` 方法接受两个参数：需要分词的字符串； 是否使用 HMM
  模型。该方法适合用于搜索引擎构建倒排索引的分词，粒度比较细
- 待分词的字符串可以是 ``unicode`` 或 ``UTF-8`` 字符串、GBK 字符串。 注意：不建议直接输入 GBK
  字符串，可能无法预料地错误解码成 UTF-8
- ``jieba.cut`` 以及 ``jieba.cut_for_search`` 返回的结构都是一个可迭代的 ``generator`` ， 可以使用
  ``for`` 循环来获得分词后得到的每一个词语(unicode)，或者用
- ``jieba.lcut`` 以及 ``jieba.lcut_for_search`` 直接返回 ``list``
- ``jieba.Tokenizer(dictionary=DEFAULT_DICT)`` 新建自定义分词器，
  可用于同时使用不同词典。\ ``jieba.dt`` 为默认分词器， 所有全局分词相关函数都是该分词器的映射。

代码示例

.. literalinclude:: ./demos/demo_usage.py
    :language: python
    :linenos:
    :lines: 2-20

:download:`点击下载完整源文件 <./demos/demo_usage.py>`

输出:

.. command-output:: python3 ./demos/demo_usage.py

*********
 添加自定义词典
*********

载入词典
====

- 开发者可以指定自己自定义的词典，以便包含 ``jieba`` 词库里没有的词。 虽然 ``jieba``
  有新词识别能力，但是自行添加新词可以保证更高的正确率
- 用法： ``jieba.load_userdict(file_name)`` # file_name 为文件类对象或自定义词典的路径
- 词典格式和 ``dict.txt`` 一样，一个词占一行； 每一行分三部分：词语、词频（可省略）、词性（可省略），用空格隔开，顺序不可颠倒。
  ``file_name`` 若为路径或二进制方式打开的文件，则文件必须为 ``UTF-8`` 编码。
- 词频省略时使用自动计算的能保证分出该词的词频。

**例如：**

::

    创新办 3 i
    云计算 5
    凱特琳 nz
    台中

- 更改分词器（默认为 ``jieba.dt``\ ）的 ``tmp_dir`` 和 ``cache_file`` 属性，
  可分别指定缓存文件所在的文件夹及其文件名，用于受限的文件系统。
- 范例：

      - 自定义词典：\ https://github.com/fxsjy/jieba/blob/master/test/userdict.txt
      - 用法示例：\ https://github.com/fxsjy/jieba/blob/master/test/test_userdict.py

            - 之前： 李小福 / 是 / 创新 / 办 / 主任 / 也 / 是 / 云 / 计算 / 方面 / 的 / 专家 /
            - 加载自定义词库后： 李小福 / 是 / 创新办 / 主任 / 也 / 是 / 云计算 / 方面 / 的 / 专家 /

调整词典
====

- 使用 ``add_word(word, freq=None, tag=None)`` 和 ``del_word(word)`` 可在程序中动态修改词典。
- 使用 ``suggest_freq(segment, tune=True)`` 可调节单个词语的词频，使其能（或不能）被分出来。
- 注意：自动计算的词频在使用 HMM 新词发现功能时可能无效。

代码示例：

::

    print('/'.join(jieba.cut('如果放到post中将出错。', HMM=False)))
    如果/放到/post/中将/出错/。
    jieba.suggest_freq(('中', '将'), True)
    494
    print('/'.join(jieba.cut('如果放到post中将出错。', HMM=False)))
    如果/放到/post/中/将/出错/。
    print('/'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False)))
    「/台/中/」/正确/应该/不会/被/切开
    jieba.suggest_freq('台中', True)
    69
    print('/'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False)))
    「/台中/」/正确/应该/不会/被/切开

- "通过用户自定义词典来增强歧义纠错能力" --- https://github.com/fxsjy/jieba/issues/14

*******
 关键词提取
*******

基于 TF-IDF 算法的关键词抽取
==================

``import jieba.analyse``

- ``jieba.analyse.extract_tags(sentence, topK=20, withWeight=False, allowPOS=())``
      - ``sentence`` 为待提取的文本
      - ``topK`` 为返回几个 TF/IDF 权重最大的关键词，默认值为 20
      - ``withWeight`` 为是否一并返回关键词权重值，默认值为 ``False``
      - ``allowPOS`` 仅包括指定词性的词，默认值为空，即不筛选
- ``jieba.analyse.TFIDF(idf_path=None)`` 新建 ``TFIDF`` 实例， ``idf_path`` 为 IDF
  频率文件

代码示例 （关键词提取）

https://github.com/fxsjy/jieba/blob/master/test/extract_tags.py

关键词提取所使用逆向文件频率（IDF）文本语料库可以切换成自定义语料库的路径

- 用法： ``jieba.analyse.set_idf_path(file_name)`` # file_name为自定义语料库的路径
- 自定义语料库示例：\ https://github.com/fxsjy/jieba/blob/master/extra_dict/idf.txt.big
- 用法示例：\ https://github.com/fxsjy/jieba/blob/master/test/extract_tags_idfpath.py

关键词提取所使用停止词（Stop Words）文本语料库可以切换成自定义语料库的路径

- 用法： ``jieba.analyse.set_stop_words(file_name)`` # file_name 为自定义语料库的路径
- 自定义语料库示例：\ https://github.com/fxsjy/jieba/blob/master/extra_dict/stop_words.txt
- 用法示例：\ https://github.com/fxsjy/jieba/blob/master/test/extract_tags_stop_words.py

关键词一并返回关键词权重值示例

- 用法示例：\ https://github.com/fxsjy/jieba/blob/master/test/extract_tags_with_weight.py

基于 TextRank 算法的关键词抽取
====================

- ``jieba.analyse.textrank(sentence, topK=20, withWeight=False, allowPOS=('ns',
  'n', 'vn', 'v'))`` 直接使用，接口相同，注意默认过滤词性。
- ``jieba.analyse.TextRank()`` 新建自定义 TextRank 实例

算法论文： [TextRank: Bringing Order into
Texts](http://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf)

基本思想:
=====

1. 将待抽取关键词的文本进行分词
2. 以固定窗口大小(默认为5，通过 ``span`` 属性调整)，词之间的共现关系，构建图
3. 计算图中节点的 ``PageRank`` ，注意是无向带权图

使用示例:
=====

见 [test/demo.py](https://github.com/fxsjy/jieba/blob/master/test/demo.py)

******
 词性标注
******

- ``jieba.posseg.POSTokenizer(tokenizer=None)`` 新建自定义分词器，\ ``tokenizer``
  参数可指定内部使用的 ``jieba.Tokenizer`` 分词器。\ ``jieba.posseg.dt`` 为默认词性标注分词器。
- 标注句子分词后每个词的词性，采用和 ``ictclas`` 兼容的标记法。
- 用法示例
- 用法示例

.. literalinclude:: ./demos/demo_pseg.py
    :language: python
    :linenos:
    :lines: 2-20

:download:`点击下载完整源文件 <./demos/demo_pseg.py>`

输出:

.. command-output:: python3 ./demos/demo_pseg.py

******
 并行分词
******

- 原理：将目标文本按行分隔后，把各行文本分配到多个 Python 进程并行分词， 然后归并结果，从而获得分词速度的可观提升
- 基于 python 自带的 ``multiprocessing`` 模块，目前暂不支持 Windows
- 用法：
      - `jieba.enable_parallel(4)` # 开启并行分词模式，参数为并行进程数
      - `jieba.disable_parallel()` # 关闭并行分词模式
- 例子：\ https://github.com/fxsjy/jieba/blob/master/test/parallel/test_file.py
- 实验结果：在 4 核 3.4GHz Linux 机器上，对金庸全集进行精确分词， 获得了 1MB/s 的速度，是单进程版的 3.3 倍。
- **注意**\ ：并行分词仅支持默认分词器 ``jieba.dt`` 和 ``jieba.posseg.dt``\ 。

****************************
 ``Tokenize`` ：返回词语在原文的起止位置
****************************

注意，输入参数只接受 ``unicode``

- 默认模式

.. literalinclude:: ./demos/demo_tokenize_default.py
    :language: python
    :linenos:
    :lines: 2-20

:download:`点击下载完整源文件 <./demos/demo_tokenize_default.py>`

输出:

.. command-output:: python3 ./demos/demo_tokenize_default.py

- 搜索模式

.. literalinclude:: ./demos/demo_tokenize_search.py
    :language: python
    :linenos:
    :lines: 2-20

:download:`点击下载完整源文件 <./demos/demo_tokenize_search.py>`

输出:

.. command-output:: python3 ./demos/demo_tokenize_search.py

*********************************
 ChineseAnalyzer for Whoosh 搜索引擎
*********************************

从核心代码中移除，放到了 ``wrapper`` 中。

- 引用： ``from jieba.analyse import ChineseAnalyzer``
- 用法示例：\ https://github.com/fxsjy/jieba/blob/master/test/test_whoosh.py

*******
 命令行分词
*******

使用示例：\ ``python -m jieba news.txt > cut_result.txt``

``python -m jieba --help`` 选项输出：

.. command-output:: python -m jieba --help

********
 延迟加载机制
********

``jieba`` 采用延迟加载，\ ``import jieba`` 和 ``jieba.Tokenizer()`` 不会立即触发词典的加载，
一旦有必要才开始加载词典构建前缀字典。如果你想手工初始 ``jieba`` ，也可以手动初始化。

在 0.28 之前的版本是不能指定主词典的路径的，有了延迟加载机制后， 你可以改变主词典的路径:

.. literalinclude:: ./demos/demo_load.py
    :language: python
    :linenos:

输出:

.. command-output:: python3 ./demos/demo_load.py

例子： https://github.com/fxsjy/jieba/blob/master/test/test_change_dictpath.py
