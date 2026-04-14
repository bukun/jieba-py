import time

import jieba

jieba.initialize()
import jieba.posseg

# url = sys.argv[1]
url = 'test/test.txt'
content = open(url, 'rb').read()
t1 = time.time()
words = list(jieba.posseg.cut(content))

t2 = time.time()
tm_cost = t2 - t1

log_f = open('1.log', 'w')
log_f.write(' / '.join(map(str, words)))

print('speed', len(content) / tm_cost, ' bytes/second')
