import time
from pathlib import Path

import jieba


def test_file_cut():
    """
    测试 jieba 对文件内容的切词。
    """
    jieba.initialize()

    # 默认使用同目录下的 test.txt
    test_file_path = Path('data/for-test/test.txt')
    assert test_file_path.exists(), f'测试文件 {test_file_path} 不存在'

    content = test_file_path.read_bytes()
    t1 = time.time()
    words = '/ '.join(jieba.cut(content))
    t2 = time.time()

    tm_cost = t2 - t1

    # 使用 pytest 断言方式
    assert words is not None
    assert len(words) > 0

    print(f'\ncost {tm_cost:.4f}s')
    if tm_cost > 0:
        print(f'speed {len(content) / tm_cost:.2f} bytes/second')


if __name__ == '__main__':
    # 保持向后兼容，如果作为脚本运行，仍然可以通过参数传入文件
    import sys

    if len(sys.argv) > 1:
        url = sys.argv[1]
        content = open(url, 'rb').read()
        t1 = time.time()
        words = '/ '.join(jieba.cut(content))
        t2 = time.time()
        tm_cost = t2 - t1
        print('cost ' + str(tm_cost))
        print('speed %s bytes/second' % (len(content) / tm_cost))
    else:
        test_file_cut()
