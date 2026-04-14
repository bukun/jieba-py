#!/usr/bin/env python

import threading
from pathlib import Path

import jieba


def test_lock():
    txt_small = Path(__file__).parent.parent / 'extra_dict/dict.txt.small'
    assert txt_small.exists()

    txt_small_path = str(txt_small.resolve())

    def inittokenizer(tokenizer, group):
        print(f'===> Thread {group}:{threading.current_thread().ident} started')
        tokenizer.initialize()
        print(f'<=== Thread {group}:{threading.current_thread().ident} finished')

    tokrs1 = [jieba.Tokenizer() for n in range(5)]
    # tokrs2 = [jieba.Tokenizer('../extra_dict/dict.txt.small') for n in range(5)]
    tokrs2 = [jieba.Tokenizer(txt_small_path) for n in range(5)]

    thr1 = [threading.Thread(target=inittokenizer, args=(tokr, 1)) for tokr in tokrs1]
    thr2 = [threading.Thread(target=inittokenizer, args=(tokr, 2)) for tokr in tokrs2]
    for thr in thr1:
        thr.start()
    for thr in thr2:
        thr.start()
    for thr in thr1:
        thr.join()
    for thr in thr2:
        thr.join()

    del tokrs1, tokrs2

    print('=' * 40)

    tokr1 = jieba.Tokenizer()
    tokr2 = jieba.Tokenizer(txt_small_path)

    thr1 = [threading.Thread(target=inittokenizer, args=(tokr1, 1)) for n in range(5)]
    thr2 = [threading.Thread(target=inittokenizer, args=(tokr2, 2)) for n in range(5)]
    for thr in thr1:
        thr.start()
    for thr in thr2:
        thr.start()
    for thr in thr1:
        thr.join()
    for thr in thr2:
        thr.join()

    assert 'QED'
    # assert tokr1.cut('我来到北京清华大学') == tokr2.cut('我来到北京清华大学')

if __name__ == '__main__':
    test_lock()