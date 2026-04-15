import sys

sys.path.append('.')

import jieba
import jieba.analyse

topK = 20

content = '''工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作'''

tags = jieba.analyse.extract_tags(content, topK=topK)

print(','.join(tags))
