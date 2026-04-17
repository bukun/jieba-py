import jieba
import jieba.posseg as pseg


class TestPosseg:
    def test_pair_creation(self):
        pair = pseg.pair('测试', 'n')
        assert pair.word == '测试'
        assert pair.flag == 'n'

    def test_pair_repr(self):
        pair = pseg.pair('测试', 'n')
        assert '测试' in repr(pair)
        assert 'n' in repr(pair)

    def test_pair_str(self):
        pair = pseg.pair('测试', 'n')
        assert str(pair) == '测试/n'

    def test_pair_iter(self):
        pair = pseg.pair('测试', 'n')
        word, flag = pair
        assert word == '测试'
        assert flag == 'n'

    def test_pair_lt(self):
        pair1 = pseg.pair('a', 'n')
        pair2 = pseg.pair('b', 'n')
        assert pair1 < pair2

    def test_pair_eq(self):
        pair1 = pseg.pair('测试', 'n')
        pair2 = pseg.pair('测试', 'n')
        assert pair1 == pair2

    def test_pair_hash(self):
        pair1 = pseg.pair('测试', 'n')
        pair2 = pseg.pair('测试', 'v')
        assert hash(pair1) == hash(pair2)

    def test_pair_encode(self):
        pair = pseg.pair('测试', 'n')
        result = pair.encode('utf-8')
        assert isinstance(result, bytes)

    def test_postokenizer_creation(self):
        tokenizer = pseg.POSTokenizer()
        assert tokenizer is not None

    def test_postokenizer_with_custom_tokenizer(self):
        custom_tokenizer = jieba.Tokenizer()
        tokenizer = pseg.POSTokenizer(custom_tokenizer)
        assert tokenizer is not None

    def test_postokenizer_repr(self):
        tokenizer = pseg.POSTokenizer()
        assert 'POSTokenizer' in repr(tokenizer)

    def test_posseg_cut_basic(self):
        result = list(pseg.cut('今天天气不错'))
        assert isinstance(result, list)
        assert len(result) > 0

    def test_posseg_lcut(self):
        result = pseg.lcut('今天天气不错')
        assert isinstance(result, list)
        assert len(result) > 0

    def test_posseg_cut_empty(self):
        result = list(pseg.cut(''))
        assert result == []

    def test_posseg_cut_with_english(self):
        result = list(pseg.cut('hello world'))
        assert isinstance(result, list)

    def test_posseg_cut_with_numbers(self):
        result = list(pseg.cut('测试123'))
        assert isinstance(result, list)


class TestViterbiPosseg:
    def test_get_top_states(self):
        t_state_v = {'a': 0.5, 'b': 0.3, 'c': 0.2, 'd': 0.1}
        result = pseg.get_top_states(t_state_v, K=3)
        assert result == ['a', 'b', 'c']


class TestDefaultInstance:
    def test_dt_exists(self):
        assert pseg.dt is not None

    def test_initialize_function(self):
        pseg.initialize()
        assert True
