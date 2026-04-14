# from __future__ import print_function

# sys.path.append("../")
import jieba.posseg as pseg


def test_cut_pos():
    words = pseg.cut('又跛又啞')
    for w in words:
        print(w.word, w.flag)
