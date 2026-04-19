# Tokenize ：返回词语在原文的起止位置
# 注意，输入参数只接受 unicode
# 默认模式
import jieba

result = jieba.tokenize('永和服装饰品有限公司')
for tk in result:
    print(f'word {tk[0]}\t\t start: {tk[1]} \t\t end:{tk[2]}')
