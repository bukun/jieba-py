==========================
原文档其他内容
==========================

原文档的其他内容，暂时保存到这里。
很多资源已经有变化，内容的修改，增删需要时间进行排查。

友情链接
=========

* https://github.com/baidu/lac   百度中文词法分析（分词+词性+专名）系统
* https://github.com/baidu/AnyQ  百度FAQ自动问答系统
* https://github.com/baidu/Senta 百度情感识别系统

系统集成
========

1. Solr: https://github.com/sing1ee/jieba-solr

分词速度
=========

* 1.5 MB / Second in Full Mode
* 400 KB / Second in Default Mode
* 测试环境: Intel(R) Core(TM) i7-2600 CPU @ 3.4GHz；《围城》.txt

常见问题
=========

1. 模型的数据是如何生成的？

详见： https://github.com/fxsjy/jieba/issues/7

2. “台中”总是被切成“台 中”？（以及类似情况）

P(台中) ＜ P(台)×P(中)，“台中”词频不够导致其成词概率较低

解决方法：强制调高词频

`jieba.add_word('台中')` 或者 `jieba.suggest_freq('台中', True)`

3. “今天天气 不错”应该被切成“今天 天气 不错”？（以及类似情况）

解决方法：强制调低词频

`jieba.suggest_freq(('今天', '天气'), True)`

或者直接删除该词 `jieba.del_word('今天天气')`

4. 切出了词典中没有的词语，效果不理想？

解决方法：关闭新词发现

`jieba.cut('丰田太省了', HMM=False)`
`jieba.cut('我们中出了一个叛徒', HMM=False)`

**更多问题请点击**：https://github.com/fxsjy/jieba/issues?sort=updated&state=closed

修订历史
==========

https://github.com/fxsjy/jieba/blob/master/Changelog

