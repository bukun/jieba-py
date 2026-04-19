# 词性标注
import jieba.posseg as pseg

words = pseg.cut('我爱北京天安门')  # jieba默认模式
for word, flag in words:
    print(f'{word} {flag}')
