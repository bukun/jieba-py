from jieba import finalseg


class TestFinalseg:
    def test_viterbi(self):
        result = finalseg.viterbi(
            '今天',
            'BMES',
            {'B': 0, 'M': -1, 'S': -2, 'E': -1},
            {'B': {'E': 0, 'M': -1}, 'M': {'B': -1, 'M': -1}, 'S': {'S': 0, 'E': -1}, 'E': {'B': -1, 'M': -1}},
            {'B': {'今': -1}, 'M': {'天': -1}, 'S': {'今': -1, '天': -1}, 'E': {'天': -1}},
        )
        assert isinstance(result, tuple)
        assert len(result) == 2

    def test_add_force_split(self):
        finalseg.add_force_split('测试词')
        assert '测试词' in finalseg.Force_Split_Words

    def test_cut_basic(self):
        result = list(finalseg.cut('今天天气不错'))
        assert isinstance(result, list)
        assert len(result) > 0

    def test_cut_empty(self):
        result = list(finalseg.cut(''))
        assert result == []

    def test_cut_with_numbers(self):
        result = list(finalseg.cut('测试123'))
        assert isinstance(result, list)

    def test_cut_with_english(self):
        result = list(finalseg.cut('hello'))
        assert isinstance(result, list)

    def test_cut_all_chinese(self):
        result = list(finalseg.cut('中文分词测试'))
        assert isinstance(result, list)

    def test_cut_mixed(self):
        result = list(finalseg.cut('今天hello天气'))
        assert isinstance(result, list)


class TestPrevStatus:
    def test_prev_status_mapping(self):
        assert finalseg.PrevStatus == {'B': 'ES', 'M': 'MB', 'S': 'SE', 'E': 'BM'}

    def test_prev_status_B(self):
        assert finalseg.PrevStatus['B'] == 'ES'

    def test_prev_status_M(self):
        assert finalseg.PrevStatus['M'] == 'MB'

    def test_prev_status_S(self):
        assert finalseg.PrevStatus['S'] == 'SE'

    def test_prev_status_E(self):
        assert finalseg.PrevStatus['E'] == 'BM'
