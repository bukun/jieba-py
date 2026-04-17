import pytest

import jieba
from jieba import Tokenizer


class TestTokenizerInit:
    def test_tokenizer_default_dict(self):
        t = Tokenizer()
        assert t.dictionary is None

    def test_tokenizer_custom_dict(self):
        t = Tokenizer('/tmp/test.txt')
        assert t.dictionary is not None

    def test_tokenizer_repr(self):
        t = Tokenizer()
        assert 'Tokenizer' in repr(t)


class TestTokenizerCut:
    def test_cut_basic(self):
        t = Tokenizer()
        result = list(t.cut('今天天气不错'))
        assert isinstance(result, list)
        assert len(result) > 0

    def test_cut_all_true(self):
        t = Tokenizer()
        result = list(t.cut('今天天气不错', cut_all=True))
        assert isinstance(result, list)

    def test_cut_hmm_false(self):
        t = Tokenizer()
        result = list(t.cut('今天天气不错', HMM=False))
        assert isinstance(result, list)

    def test_cut_empty(self):
        t = Tokenizer()
        result = list(t.cut(''))
        assert result == []

    def test_lcut(self):
        t = Tokenizer()
        result = t.lcut('今天天气不错')
        assert isinstance(result, list)

    def test_cut_for_search(self):
        t = Tokenizer()
        result = list(t.cut_for_search('今天天气不错'))
        assert isinstance(result, list)

    def test_lcut_for_search(self):
        t = Tokenizer()
        result = t.lcut_for_search('今天天气不错')
        assert isinstance(result, list)


class TestTokenizerWordDict:
    def test_add_word(self):
        t = Tokenizer()
        t.initialize()
        t.add_word('测试词', 10)
        assert '测试词' in t.FREQ

    def test_del_word(self):
        t = Tokenizer()
        t.initialize()
        t.del_word('测试词')
        assert '测试词' in t.FREQ

    def test_suggest_freq(self):
        t = Tokenizer()
        t.initialize()
        freq = t.suggest_freq('今天天气')
        assert isinstance(freq, int)

    def test_suggest_freq_with_tune(self):
        t = Tokenizer()
        t.initialize()
        freq = t.suggest_freq('今天天气', tune=True)
        assert isinstance(freq, int)


class TestTokenizerDAG:
    def test_get_DAG(self):
        t = Tokenizer()
        t.initialize()
        dag = t.get_DAG('今天')
        assert isinstance(dag, dict)

    def test_calc(self):
        t = Tokenizer()
        t.initialize()
        dag = {0: [0], 1: [1]}
        route = {}
        t.calc('今天', dag, route)
        assert len(route) > 0


class TestTokenizerTokenize:
    def test_tokenize_basic(self):
        t = Tokenizer()
        t.initialize()
        result = list(t.tokenize('今天天气不错'))
        assert isinstance(result, list)

    def test_tokenize_search_mode(self):
        t = Tokenizer()
        t.initialize()
        result = list(t.tokenize('今天天气不错', mode='search'))
        assert isinstance(result, list)

    def test_tokenize_hmm_false(self):
        t = Tokenizer()
        t.initialize()
        result = list(t.tokenize('今天天气不错', HMM=False))
        assert isinstance(result, list)


class TestTokenizerDictionary:
    def test_set_dictionary(self, tmp_path):
        t = Tokenizer()
        dict_file = tmp_path / 'test_dict.txt'
        dict_file.write_text('测试 10\n')
        t.set_dictionary(str(dict_file))
        assert t.initialized is False

    def test_set_dictionary_nonexistent(self):
        t = Tokenizer()
        with pytest.raises(Exception):
            t.set_dictionary('/nonexistent/path.txt')


class TestTokenizerUserdict:
    def test_load_userdict_from_file(self, tmp_path):
        t = Tokenizer()
        t.initialize()
        dict_file = tmp_path / 'userdict.txt'
        dict_file.write_text('用户词典 20\n')
        t.load_userdict(str(dict_file))
        assert '用户词典' in t.FREQ

    def test_load_userdict_from_file_object(self, tmp_path):
        t = Tokenizer()
        t.initialize()
        dict_file = tmp_path / 'userdict.txt'
        dict_file.write_text('测试词 15\n')
        with open(dict_file, 'rb') as f:
            t.load_userdict(f)
        assert '测试词' in t.FREQ


class TestGlobalFunctions:
    def test_cut(self):
        result = list(jieba.cut('今天天气不错'))
        assert isinstance(result, list)

    def test_lcut(self):
        result = jieba.lcut('今天天气不错')
        assert isinstance(result, list)

    def test_cut_for_search(self):
        result = list(jieba.cut_for_search('今天天气不错'))
        assert isinstance(result, list)

    def test_lcut_for_search(self):
        result = jieba.lcut_for_search('今天天气不错')
        assert isinstance(result, list)

    def test_add_word(self):
        jieba.add_word('测试词', 10)
        assert '测试词' in jieba.dt.FREQ

    def test_del_word(self):
        jieba.del_word('测试词')
        assert '测试词' in jieba.dt.FREQ

    def test_get_FREQ(self):
        freq = jieba.get_FREQ('今天')
        assert freq is not None

    def test_tokenize(self):
        result = list(jieba.tokenize('今天天气不错'))
        assert isinstance(result, list)

    def test_suggest_freq(self):
        freq = jieba.suggest_freq('今天')
        assert isinstance(freq, int)


class TestVersion:
    def test_version_exists(self):
        assert jieba.__version__ is not None


class TestSetLogLevel:
    def test_set_log_level(self):
        jieba.setLogLevel(0)
        assert True
