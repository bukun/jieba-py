# 搜索模式
import jieba

result = jieba.tokenize('永和服装饰品有限公司', mode='search')
for tk in result:
    print(f'word {tk[0]}\t\t start: {tk[1]} \t\t end:{tk[2]}')
