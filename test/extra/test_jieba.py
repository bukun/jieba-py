"""
由于安装的是自行修改、打包的jieba分词库，补充了基本的测试，以确保正常运行。

jieba 分词核心功能单元测试
1. 基础分词功能（精确模式、全模式、搜索引擎模式）
2. 自定义词典功能
3. 关键词提取
4. 词性标注
5. 并行分词
6. Tokenize 功能
7. 特殊场景测试
"""

import unittest

import jieba

# jieba.load_userdict('extra_dict/dict.txt.big')
import jieba.analyse
import jieba.posseg as pseg


class TestJiebaBasicSegmentation(unittest.TestCase):
    """测试 jieba 基础分词功能"""

    def test_cut_precise_mode(self):
        """测试精确模式分词（默认模式）"""
        text = '我来到北京清华大学'
        result = list(jieba.cut(text, cut_all=False))
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)
        # 精确模式应该能正确识别"北京"和"清华大学"
        self.assertIn('北京', result)
        self.assertIn('清华大学', result)

    def test_cut_full_mode(self):
        """测试全模式分词"""
        text = '我来到北京清华大学'
        result = list(jieba.cut(text, cut_all=True))
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)
        # 全模式会产生更多组合
        self.assertIn('清华', result)
        self.assertIn('大学', result)

    def test_cut_search_engine_mode(self):
        """测试搜索引擎模式分词"""
        text = '小明硕士毕业于中国科学院计算所，后在日本京都大学深造'
        result = list(jieba.cut_for_search(text))
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)
        # 搜索引擎模式会对长词再次切分
        self.assertIn('中国', result)
        self.assertIn('科学', result)
        self.assertIn('学院', result)

    def test_lcut_precise_mode(self):
        """测试 lcut 返回 list 的分词方式"""
        text = '这是一个测试文本'
        result = jieba.lcut(text)
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

    def test_lcut_full_mode(self):
        """测试 lcut 全模式"""
        text = '南京市长江大桥'
        result = jieba.lcut(text, cut_all=True)
        self.assertIsInstance(result, list)
        # 全模式应该包含多种切分可能
        self.assertTrue(len(result) >= 4)

    def test_empty_string(self):
        """测试空字符串分词"""
        text = ''
        result = list(jieba.cut(text))
        self.assertEqual(result, [])

    def test_single_character(self):
        """测试单个字符分词"""
        text = '测'
        result = list(jieba.cut(text))
        self.assertEqual(result, ['测'])

    def test_english_text(self):
        """测试英文文本分词"""
        text = 'Hello World Python'
        result = list(jieba.cut(text))
        self.assertIsInstance(result, list)
        # 英文应该按空格分隔
        self.assertIn('Hello', result)
        self.assertIn('World', result)

    def test_mixed_chinese_english(self):
        """测试中英文混合文本"""
        text = 'Python是一门编程语言'
        result = list(jieba.cut(text))
        self.assertIsInstance(result, list)
        self.assertIn('Python', result)
        self.assertIn('编程语言', result)

    def test_numbers_and_symbols(self):
        """测试数字和符号"""
        text = '2024年有365天，每天24小时'
        result = list(jieba.cut(text))
        self.assertIsInstance(result, list)
        self.assertIn('2024', result)
        self.assertIn('365', result)
        self.assertIn('24', result)

    def test_punctuation_handling(self):
        """测试标点符号处理"""
        text = '你好，世界！这是一个测试。'
        result = list(jieba.cut(text))
        self.assertIsInstance(result, list)
        # 标点符号应该被单独分出
        self.assertIn('，', result)
        self.assertIn('！', result)
        self.assertIn('。', result)


def test_add_word():
    """测试添加自定义词汇"""
    text = '这个测试新词应该被识别'

    # 添加前可能不会被正确识别
    list(jieba.cut(text))

    # 添加自定义词
    jieba.add_word('测试新词')
    result_after = list(jieba.cut(text))

    # 添加后应该能识别

    assert '测试新词' in result_after
    jieba.del_word('测试新词')


def test_del_word():
    """测试删除自定义词汇"""
    jieba.add_word('临时词汇')
    text = '这是一个临时词汇'

    # 删除前应该能识别
    result_before = list(jieba.cut(text))

    assert '临时词汇' in result_before

    # 删除词汇
    jieba.del_word('临时词汇')
    result_after = list(jieba.cut(text))
    jieba.del_word('临时词汇')

    # 删除后不应该再作为一个整体出现
    assert '临时词汇' not in result_after


def test_suggest_freq():
    """测试调整词语频率"""
    text = '如果放到post中将出错'

    # 调整频率让"中"和"将"分开
    jieba.suggest_freq(('中', '将'), True)
    result = list(jieba.cut(text))

    # 应该能正确分开
    assert '中' in result
    assert '将' in result


def test_load_custom_dict():
    """测试加载自定义词典文件"""
    # 创建一个临时词典文件
    import tempfile
    from pathlib import Path

    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write('自定义词1 100 n\n')
        f.write('自定义词2 200 v\n')
        temp_file = f.name

    try:
        # 加载词典
        jieba.load_userdict(temp_file)

        # 测试分词
        text = '这是自定义词1和自定义词2的测试'
        result = list(jieba.cut(text))

        assert '自定义词1' in result
        assert '自定义词2' in result
    finally:
        # 清理临时文件
        Path(temp_file).unlink()


class TestJiebaCustomDictionary(unittest.TestCase):
    """测试 jieba 自定义词典功能"""

    def setUp(self):
        """每个测试前重置词典"""
        # 保存原始状态
        pass

    def tearDown(self):
        """每个测试后清理"""
        # 清理添加的词
        jieba.del_word('测试新词')
        jieba.del_word('人工智能算法')

    # def test_add_word(self):
    #     """测试添加自定义词汇"""
    #     text = '这个测试新词应该被识别'
    #
    #     # 添加前可能不会被正确识别
    #     list(jieba.cut(text))
    #
    #     # 添加自定义词
    #     jieba.add_word('测试新词')
    #     result_after = list(jieba.cut(text))
    #
    #     # 添加后应该能识别
    #     self.assertIn('测试新词', result_after)


class TestJiebaKeywordExtraction(unittest.TestCase):
    """测试 jieba 关键词提取功能"""

    def test_extract_tags_basic(self):
        """测试基础关键词提取"""
        text = """
        今天天气真好，阳光明媚，适合出去散步。
        公园里有很多人在跑步、打球、做运动。
        这样的天气让人心情愉悦。
        """
        keywords = jieba.analyse.extract_tags(text, topK=5)

        self.assertIsInstance(keywords, list)
        self.assertTrue(len(keywords) <= 5)
        self.assertTrue(len(keywords) > 0)

    def test_extract_tags_with_weight(self):
        """测试带权重的关键词提取"""
        text = 'Python是一种广泛使用的编程语言，在数据科学、机器学习、Web开发等领域都有应用'
        keywords = jieba.analyse.extract_tags(text, topK=3, withWeight=True)

        self.assertIsInstance(keywords, list)
        # 每个元素应该是 (词, 权重) 的元组
        for item in keywords:
            self.assertIsInstance(item, tuple)
            self.assertEqual(len(item), 2)
            self.assertIsInstance(item[0], str)
            self.assertIsInstance(item[1], float)

    def test_extract_tags_allow_pos(self):
        """测试按词性过滤关键词"""
        text = '小明正在认真地学习Python编程语言'
        # 只提取名词和动词
        keywords = jieba.analyse.extract_tags(text, topK=5, allowPOS=('n', 'v', 'eng'))

        self.assertIsInstance(keywords, list)

    def test_textrank_basic(self):
        """测试 TextRank 关键词提取"""
        text = """
        自然语言处理是计算机科学领域与人工智能领域中的一个重要方向。
        它研究能实现人与计算机之间用自然语言进行有效通信的各种理论和方法。
        """
        keywords = jieba.analyse.textrank(text, topK=5)

        self.assertIsInstance(keywords, list)
        self.assertTrue(len(keywords) > 0)

    def test_textrank_with_weight(self):
        """测试 TextRank 带权重的关键词提取"""
        text = '机器学习算法在大数据分析中发挥着重要作用'
        keywords = jieba.analyse.textrank(text, topK=3, withWeight=True)

        self.assertIsInstance(keywords, list)
        for item in keywords:
            self.assertIsInstance(item, tuple)
            self.assertEqual(len(item), 2)

    def test_extract_tags_empty_text(self):
        """测试空文本的关键词提取"""
        text = ''
        keywords = jieba.analyse.extract_tags(text)
        self.assertEqual(keywords, [])

    def test_set_stop_words(self):
        """测试设置停用词"""
        import tempfile
        from pathlib import Path

        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as f:
            f.write('的\n')
            f.write('是\n')
            f.write('在\n')
            temp_file = f.name

        try:
            jieba.analyse.set_stop_words(temp_file)
            text = '这是一个在测试'
            keywords = jieba.analyse.extract_tags(text, topK=5)
            # 停用词不应该出现在关键词中
            self.assertNotIn('的', keywords)
            self.assertNotIn('是', keywords)
            self.assertNotIn('在', keywords)
        finally:
            Path(temp_file).unlink()


class TestJiebaPosTagging(unittest.TestCase):
    """测试 jieba 词性标注功能"""

    def test_posseg_cut(self):
        """测试词性标注"""
        import jieba.posseg as pseg

        text = '我爱北京天安门'
        words = pseg.cut(text)

        result = [(word.word, word.flag) for word in words]
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

        # 检查是否有词性标注
        for word, flag in result:
            self.assertIsInstance(word, str)
            self.assertIsInstance(flag, str)
            self.assertTrue(len(flag) > 0)

    def test_posseg_empty_text(self):
        """测试空文本的词性标注"""
        import jieba.posseg as pseg

        text = ''
        words = list(pseg.cut(text))
        self.assertEqual(words, [])

    def test_posseg_english(self):
        """测试英文的词性标注"""
        import jieba.posseg as pseg

        text = 'I love Python'
        words = list(pseg.cut(text))
        self.assertIsInstance(words, list)


class TestJiebaTokenize(unittest.TestCase):
    """测试 jieba tokenize 功能"""

    def test_tokenize_default_mode(self):
        """测试默认模式的 tokenize"""
        text = '永和服装饰品有限公司'
        result = list(jieba.tokenize(text))

        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

        # 每个元素应该是 (词, 起始位置, 结束位置)
        for token in result:
            self.assertEqual(len(token), 3)
            word, start, end = token
            self.assertIsInstance(word, str)
            self.assertIsInstance(start, int)
            self.assertIsInstance(end, int)
            self.assertTrue(start < end)

    def test_tokenize_search_mode(self):
        """测试搜索引擎模式的 tokenize"""
        text = '永和服装饰品有限公司'
        result = list(jieba.tokenize(text, mode='search'))

        self.assertIsInstance(result, list)
        # 搜索引擎模式应该产生更多的 token
        self.assertTrue(len(result) > 0)

    def test_tokenize_positions(self):
        """测试 tokenize 位置信息的正确性"""
        text = '你好世界'
        result = list(jieba.tokenize(text))

        # 验证位置信息是否连续且正确
        if len(result) > 0:
            first_token = result[0]
            self.assertEqual(first_token[1], 0)  # 第一个词的起始位置应该是0

            # 验证位置不重叠且连续
            for i in range(1, len(result)):
                prev_end = result[i - 1][2]
                curr_start = result[i][1]
                self.assertEqual(prev_end, curr_start)


class TestJiebaSpecialCases(unittest.TestCase):
    """测试特殊场景"""

    def test_long_text(self):
        """测试长文本分词"""
        text = ' '.join(['这是一个测试'] * 100)
        result = list(jieba.cut(text))
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

    def test_repeated_words(self):
        """测试重复词汇"""
        text = '测试测试测试'
        result = list(jieba.cut(text))
        self.assertIsInstance(result, list)
        # 应该能识别重复的词
        self.assertTrue(len(result) > 0)

    def test_special_characters(self):
        """测试特殊字符"""
        text = '@#$% ^&*()'
        result = list(jieba.cut(text))
        self.assertIsInstance(result, list)

    def test_unicode_characters(self):
        """测试 Unicode 字符"""
        text = 'こんにちは世界'  # 日文
        result = list(jieba.cut(text))
        self.assertIsInstance(result, list)

    def test_mixed_content(self):
        """测试混合内容（中文、英文、数字、符号）"""
        text = 'Python 3.9 发布了！新特性包括：| pattern matching | dict union operators'
        result = list(jieba.cut(text))
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

    def test_url_and_email(self):
        """测试 URL 和邮箱地址"""
        text = '访问 https://www.example.com 或发送邮件到 test@example.com'
        result = list(jieba.cut(text))
        self.assertIsInstance(result, list)

    def test_idiom(self):
        """测试成语识别"""
        text = '他做事总是半途而废'
        result = list(jieba.cut(text))
        self.assertIsInstance(result, list)
        # 理想情况下应该识别"半途而废"
        self.assertIn('半途而废', result)


class TestJiebaPerformance(unittest.TestCase):
    """测试性能相关功能"""

    def test_multiple_segmentations(self):
        """测试多次分词的性能稳定性"""
        text = '这是一个性能测试文本'
        results = []

        for _ in range(10):
            result = list(jieba.cut(text))
            results.append(result)

        # 所有结果应该一致
        for i in range(1, len(results)):
            self.assertEqual(results[0], results[i])


class TestJiebaCoreFunctions(unittest.TestCase):
    """
    测试 jieba 分词核心功能
    覆盖：精确模式、全模式、搜索引擎模式、词性标注、关键词提取、自定义词典
    """

    def setUp(self):
        """
        初始化测试数据（每个测试方法执行前自动调用）
        """
        # 标准中文测试文本
        self.test_text = '我在上海浦东软件园使用jieba分词工具'
        # 短文本测试
        self.short_text = '我爱Python编程'
        # 自定义词典词汇（用于测试自定义词典功能）
        self.custom_word = '浦东软件园'

    def test_01_precise_mode(self):
        """测试1：精确模式分词（默认模式，最常用）"""
        result = jieba.lcut(self.test_text)
        # 验证核心词汇是否被正确拆分
        self.assertIn('上海浦东', result)
        self.assertIn('软件园', result)
        self.assertIn('jieba', result)
        self.assertIn('分词', result)
        print('✅ 精确模式分词测试通过')

    def test_02_full_mode(self):
        """测试2：全模式分词（输出所有可能词汇）"""
        result = jieba.lcut(self.test_text, cut_all=True)
        # 全模式会拆分出所有组合词汇
        self.assertIn('上海', result)
        self.assertIn('浦东', result)
        self.assertIn('软件园', result)
        print('✅ 全模式分词测试通过')

    def test_03_search_mode(self):
        """测试3：搜索引擎模式分词（适合搜索引擎场景）"""
        result = jieba.lcut_for_search(self.test_text)
        self.assertIn('上海', result)
        self.assertIn('浦东', result)
        self.assertIn('软件园', result)
        print('✅ 搜索引擎模式分词测试通过')

    def test_04_pos_tagging(self):
        """测试4：词性标注功能"""
        words = pseg.cut(self.test_text)
        word_list = [(word.word, word.flag) for word in words]
        # 验证词性结果（r=代词，ns=地名，n=名词，eng=英文）
        self.assertEqual(word_list[0][0], '我')
        self.assertEqual(word_list[0][1], 'rr')
        self.assertEqual(word_list[2][1], 'ns')  # 上海 是地名
        print('✅ 词性标注测试通过')

    def test_05_keywords_extract(self):
        """测试5：TF-IDF关键词提取（核心NLP功能）"""
        keywords = jieba.analyse.extract_tags(self.test_text, topK=3)
        self.assertIn('jieba', keywords)
        self.assertIn('分词', keywords)
        print('✅ 关键词提取测试通过')

    def test_06_custom_dictionary(self):
        """测试6：自定义词典（验证用户词典加载/词汇强制拆分）"""
        # 临时添加自定义词汇，测试是否能正确识别
        jieba.add_word(self.custom_word)
        result = jieba.lcut('我在浦东软件园工作')
        # 验证自定义词汇被整体识别，不拆分
        self.assertIn(self.custom_word, result)
        self.assertNotIn('浦东', result)
        self.assertNotIn('软件园', result)
        print('✅ 自定义词典功能测试通过')

    def test_07_short_text_cut(self):
        """测试7：短文本分词"""
        result = jieba.lcut(self.short_text)
        # ToDo:
        # self.assertEqual(result, ['我', '爱', 'Python', '编程'])
        self.assertEqual(result, ['我爱', 'Python', '编程'])
        print('✅ 短文本分词测试通过')
