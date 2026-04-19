from jieba import _compat


class TestCompat:
    def test_strdecode_str(self):
        result = _compat.strdecode('测试')
        assert result == '测试'

    def test_strdecode_bytes_utf8(self):
        result = _compat.strdecode(b'\xe6\xb5\x8b\xe8\xaf\x95')
        assert result == '测试'

    def test_strdecode_bytes_gbk(self):
        result = _compat.strdecode('测试'.encode('gbk'))
        assert result == '测试'

    def test_resolve_filename_file_object(self):
        import io

        f = io.BytesIO(b'test')
        f.name = 'test.txt'
        assert _compat.resolve_filename(f) == 'test.txt'

    def test_resolve_filename_no_name(self):
        import io

        f = io.BytesIO(b'test')
        result = _compat.resolve_filename(f)
        assert 'BytesIO' in result

    def test_iterkeys(self):
        d = {'a': 1, 'b': 2}
        result = list(_compat.iterkeys(d))
        assert result == ['a', 'b']

    def test_itervalues(self):
        d = {'a': 1, 'b': 2}
        result = list(_compat.itervalues(d))
        assert result == [1, 2]

    def test_iteritems(self):
        d = {'a': 1, 'b': 2}
        result = list(_compat.iteritems(d))
        assert result == [('a', 1), ('b', 2)]

    def test_text_type(self):
        assert _compat.text_type is str

    def test_string_types(self):
        assert _compat.string_types == (str,)

    def test_set_log_level(self):
        _compat.setLogLevel(0)
        assert True

    def test_get_module_res(self):
        f = _compat.get_module_res('_data', 'dict.txt')
        assert f is not None
        f.close()
