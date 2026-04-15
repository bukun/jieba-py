import sys; sys.path.append('.') ; sys.path.append('..')

import jieba

# 改变主词典的路径:
jieba.set_dictionary("./demos/dict_demo.txt")

# 手动初始化（可选）
jieba.initialize() 