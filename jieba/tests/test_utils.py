from jieba import utils


class TestUtils:
    def test_re_userdict(self):
        assert utils.re_userdict.match('测试 10 n')
        assert utils.re_userdict.match('测试 10')
        assert utils.re_userdict.match('测试')
        assert not utils.re_userdict.match('')

    def test_re_eng_default(self):
        assert utils.re_eng_default.match('a')
        assert utils.re_eng_default.match('A')
        assert utils.re_eng_default.match('1')
        assert not utils.re_eng_default.match('中')

    def test_re_han_default(self):
        assert utils.re_han_default.match('测试')
        assert utils.re_han_default.match('hello')
        assert not utils.re_han_default.match('   ')

    def test_re_skip_default(self):
        assert utils.re_skip_default.match(' ')
        assert utils.re_skip_default.match('\r\n')
        assert not utils.re_skip_default.match('abc')

    def test_re_han_final(self):
        assert utils.re_han_final.match('中文')

    def test_re_skip_final(self):
        assert utils.re_skip_final.match('123')
        assert utils.re_skip_final.match('12.5%')

    def test_re_han_detail(self):
        assert utils.re_han_detail.match('中文')

    def test_re_skip_detail(self):
        assert utils.re_skip_detail.match('123')
        assert utils.re_skip_detail.match('abc')

    def test_re_han_internal(self):
        assert utils.re_han_internal.match('中文')

    def test_re_skip_internal(self):
        assert utils.re_skip_internal.match(' ')

    def test_re_eng_pos(self):
        assert utils.re_eng_pos.match('abc123')

    def test_re_num_pos(self):
        assert utils.re_num_pos.match('123')
        assert utils.re_num_pos.match('.5')

    def test_re_eng1_pos(self):
        assert utils.re_eng1_pos.match('a')
        assert utils.re_eng1_pos.match('1')
        assert not utils.re_eng1_pos.match('ab')
