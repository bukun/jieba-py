import jieba


def cuttest(test_sent, g_mode):

    result = jieba.tokenize(test_sent, mode=g_mode)
    count = 0
    for tk in result:
        count += 1
        print(f'word {tk[0]}\t\t start: {tk[1]} \t\t end:{tk[2]}')
    return count


def test_run(test_data):
    for m in ('default', 'search'):
        for tester in test_data:
            if tester:
                assert cuttest(tester, m) > 0
            else:
                assert cuttest(tester, m) == 0
