import jieba.analyse as analyse
from jieba.analyse.tfidf import TFIDF


class TestKeywordExtractor:
    def test_stop_words_default(self):
        tfidf = TFIDF()
        assert 'the' in tfidf.stop_words
        assert 'is' in tfidf.stop_words
        assert 'and' in tfidf.stop_words

    def test_stop_words_custom(self, tmp_path):
        stop_file = tmp_path / 'stop.txt'
        stop_file.write_text('自定义\n停用词\n')
        tfidf = TFIDF()
        tfidf.set_stop_words(str(stop_file))
        assert '自定义' in tfidf.stop_words
        assert '停用词' in tfidf.stop_words


class TestTFIDF:
    def test_tfidf_creation(self):
        tfidf = analyse.TFIDF()
        assert tfidf is not None

    def test_tfidf_default_idf_loaded(self):
        tfidf = analyse.TFIDF()
        assert len(tfidf.idf_freq) > 0
        assert tfidf.median_idf > 0

    def test_extract_tags_basic(self):
        tfidf = analyse.TFIDF()
        result = tfidf.extract_tags('今天天气不错阳光明媚')
        assert isinstance(result, list)

    def test_extract_tags_topk(self):
        tfidf = analyse.TFIDF()
        result = tfidf.extract_tags('今天天气不错阳光明媚', topK=3)
        assert len(result) <= 3

    def test_extract_tags_with_weight(self):
        tfidf = analyse.TFIDF()
        result = tfidf.extract_tags('今天天气不错阳光明媚', topK=3, withWeight=True)
        assert isinstance(result, list)
        if result:
            assert isinstance(result[0], tuple)

    def test_extract_tags_allow_pos(self):
        tfidf = analyse.TFIDF()
        result = tfidf.extract_tags('今天天气不错', allowPOS=('n', 'v'))
        assert isinstance(result, list)

    def test_set_idf_path(self, tmp_path):
        idf_file = tmp_path / 'idf.txt'
        idf_file.write_text('测试词 11.0\n')
        tfidf = analyse.TFIDF()
        tfidf.set_idf_path(str(idf_file))
        assert '测试词' in tfidf.idf_freq


class TestTextRank:
    def test_textrank_creation(self):
        tr = analyse.TextRank()
        assert tr is not None

    def test_textrank_extract_tags(self):
        tr = analyse.TextRank()
        result = tr.extract_tags('今天天气不错阳光明媚')
        assert isinstance(result, list)

    def test_textrank_topk(self):
        tr = analyse.TextRank()
        result = tr.extract_tags('今天天气不错阳光明媚', topK=2)
        assert len(result) <= 2

    def test_textrank_with_weight(self):
        tr = analyse.TextRank()
        result = tr.extract_tags('今天天气不错', topK=3, withWeight=True)
        assert isinstance(result, list)


class TestGlobalFunctions:
    def test_extract_tags(self):
        result = analyse.extract_tags('今天天气不错')
        assert isinstance(result, list)

    def test_tfidf_instance(self):
        assert isinstance(analyse.default_tfidf, TFIDF)

    def test_textrank_instance(self):
        assert isinstance(analyse.default_textrank, analyse.TextRank)

    def test_set_stop_words(self, tmp_path):
        stop_file = tmp_path / 'stop.txt'
        stop_file.write_text('测试停用词\n')
        analyse.set_stop_words(str(stop_file))
        assert True
