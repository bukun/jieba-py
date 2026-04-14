##########
 附录（其他问题）
##########

******
 其他词典
******

1. 占用内存较小的词典文件
   https://github.com/fxsjy/jieba/raw/master/extra_dict/dict.txt.small
2. 支持繁体分词更好的词典文件
   https://github.com/fxsjy/jieba/raw/master/extra_dict/dict.txt.big

下载你所需要的词典，然后覆盖 :file:`jieba/dict.txt` 即可； 或者用
``jieba.set_dictionary('data/dict.txt.big')``

********
 其他语言实现
********

结巴分词 Java 版本
============

作者：piaolingxue 地址：\ https://github.com/huaban/jieba-analysis

结巴分词 C++ 版本
===========

作者：yanyiwu 地址：\ https://github.com/yanyiwu/cppjieba

结巴分词 Rust 版本
============

作者：messense, MnO2 地址：\ https://github.com/messense/jieba-rs

结巴分词 Node.js 版本
===============

作者：yanyiwu 地址：\ https://github.com/yanyiwu/nodejieba

结巴分词 Erlang 版本
==============

作者：falood 地址：\ https://github.com/falood/exjieba

结巴分词 R 版本
=========

作者：qinwf 地址：\ https://github.com/qinwf/jiebaR

结巴分词 iOS 版本
===========

作者：yanyiwu 地址：\ https://github.com/yanyiwu/iosjieba

结巴分词 PHP 版本
===========

作者：fukuball 地址：\ https://github.com/fukuball/jieba-php

结巴分词 .NET(C#) 版本
================

作者：anderscui 地址：\ https://github.com/anderscui/jieba.NET/

结巴分词 Go 版本
==========

- 作者: wangbin 地址: https://github.com/wangbin/jiebago
- 作者: yanyiwu 地址: https://github.com/yanyiwu/gojieba

结巴分词Android版本
=============

- 作者 Dongliang.W 地址：\ https://github.com/452896915/jieba-android

****************
 人民日报标注语料库（PFR）
****************

PFR语料库是对人民日报1998年上半年的纯文本语料进行了词语切分和词性标注制作而成的，
严格按照人民日报的日期、版序、文章顺序编排的。
文章中的每个词语都带有词性标记。

目前的标记集里有26个基本词类标记（名词n、时间词t、处所词s、方位词f、数词m、量词q、区别词b、代词r、动词v、
形容词a、状态词z、副词d、介词p、连词c、助词u、语气词y、叹词e、拟声词o、成语i、习惯用语l、简称j、
前接成分h、后接成分k、语素g、非语素字x、标点符号w）外，
从语料库应用的角度，增加了专有名词（人名nr、地名ns、机构名称nt、其他专有名词nz）；
从语言学角度也增加了一些标记，总共使用了40多个个标记。

生语料库和熟语料库
=========

语料库中存放的是在语言的实际使用中真实出现过的语言材料， 语料库是以电子计算机为载体承载语言知识的基础资源，
真实语料需要经过加工、分析和处理之后才能成为可用的语料库。

生语料库
    是指收集之后未加工的预料库

熟语料库
    相对而言，熟语料库就是经过加工的

标记说明
====

标记说明参考：

.. code-block:: text

    代码  名称
    Ag  形语素
    a   形容词
    ad  副形词
    an  名形词
    Bg  区别语素
    b   区别词
    c   连词
    Dg  副语素
    d   副词
    e   叹词
    f   方位词
    g   语素
    h   前接成分
    i   成语
    j   简略语
    k   后接成分
    l   习用语
    Mg  数语素
    m   数词
    Ng  名语素
    n   名词
    nr  人名
    ns  地名
    nt  机构团体
    nx  外文字符
    nz  其它专名
    o   拟声词
    p   介词
    Qg  量语素
    q   量词
    Rg  代语素
    r   代词
    s   处所词
    Tg  时间语素
    t   时间词
    Ug  助语素
    u   助词
    Vg  动语素
    v   动词
    vd  副动词
    vn  名动词
    w   标点符号
    x   非语素字
    Yg  语气语素
    y   语气词
    z   状态词

from: https://cloud.tencent.com/developer/article/1091906

格式说明
====

语料是纯文本文件，文件中每一行代表一自然段或者一个标题， 一篇文章有若干个自然段，
因此在语料中一篇文章是由多行组成的。

每一行的开头是编号。
比如 ``19980101-01-001-001`` 表示这一自然段是1998年1月1日的第01版的第001篇文章的第001自然段，
用短横线隔开的4部分按照顺序是“年月日-版号-篇章号-段号”。
标号也作为一个词进行标注，词性固定为“m（数词）”。

一篇文章里面的段落之间是不空行的，在两篇文章之间，会有一个空行，表示文章的分界线，
同时，下一篇文章的“篇章号-段号”都会有所改变。
标号之后，是2个单字节空格，然后开始正文。

正文部分按照规范已经切分成词，并且加上标注， 标注的格式为“词语/词性”，即词语后面加单斜线，再紧跟词性标记。
词与词之间用2个单字节空格隔开。每段最后的词，在标记之后也有2个单字节空格，保持格式一致。
语料中除了词性标记以外，还有“短语标记”，
这种情况一般出现在机构团体名称、成语等情况中。

如“通过/p [中央/n 人民/n 广播/vn 电台/n]nt 、/w”中， 用“[ ]”合起来的部分是一个完整的机构团体名称，
方括号后面紧跟标注nt，nt之后空两个单字节空格，保持了格式的一致。

例子

.. code-block:: text

    19980101-01-001-001/m  迈向/v  充满/v  希望/n  的/u  新/a  世纪/n  ——/w  一九九八年/t  新年/t  讲话/n  （/w  附/v  图片/n  １/m  张/q  ）/w  ……  19980101-01-001-006/m  在/p  １９９８年/t  来临/v  之际/f  ，/w  我/r  十分/m  高兴/a  地/u  通过/p  [中央/n  人民/n  广播/vn  电台/n]nt  、/w  [中国/ns  国际/n  广播/vn  电台/n]nt  和/c  [中央/n  电视台/n]nt  ，/w  向/p  全国/n  各族/r  人民/n  ，/w  向/p  [中国香港/ns  特别/a  行政区/n]ns  同胞/n  、/w  中国澳门/ns  和/c  中国台湾/ns  同胞/n  、/w  海外/s  侨胞/n  ，/w  向/p  世界/n  各国/r  的/u  朋友/n  们/k  ，/w  致以/v  诚挚/a  的/u  问候/vn  和/c  良>好/a  的/u  祝愿/vn  ！/w

其他语料库汇总
=======

- http://blog.csdn.net/qq_31550425/article/details/54983414
- http://blog.csdn.net/hengwen1991/article/details/51750630
- http://blog.csdn.net/baiyi_canggou/article/details/59108547

.. https://www.heywhale.com/mw/dataset/5ce7983cd10470002b334de3

引用格式

.. code-block:: text

    @misc{PFR5215,
        title = { 1998人民日报标注语料库（PFR） }
        author = { Vivian },
        howpublished = { \url{https://www.heywhale.com/mw/dataset/5ce7983cd10470002b334de3} }
        year = { 2019 }
    }

北大中文《人民日报》199801-199806数据集介绍
============================

数据集概述

PFR语料库是在得到相关新闻信息中心许可的条件下，以1998年人民日报语料为对象制作的标注语料库。
该数据集包含了1998年1月至6月的《人民日报》语料，旨在促进中文信息处理研究的发展。

使用说明

- 数据集获取：自4月3日起，PFR语料库1月份的语料在本仓库免费公开，用户可进行下载。
- 制作规范：PFR语料库的制作遵循《现代汉语语料库加工——词语切分与词性标注规范》。
- 引用说明：在使用或引用PFR语料库的研究或论文工作中，请务必注明来源。

注意事项

- 请确保在研究和引用过程中遵循学术规范和道德准则。
- 本数据集仅用于学术研究目的，不得用于任何商业用途。
- 我们希望这个数据集能为您的学术研究提供有益的帮助。
