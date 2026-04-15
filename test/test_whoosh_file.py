# -*- coding: UTF-8 -*-
import os
import sys ; sys.path.append('.')
from whoosh.fields import *
from whoosh.index import create_in
from whoosh.qparser import QueryParser

from wrapper.analyzer import ChineseAnalyzer

analyzer = ChineseAnalyzer()

schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored=True, analyzer=analyzer))
if not os.path.exists('tmp'):
    os.mkdir('tmp')
ix = create_in('tmp', schema)
writer = ix.writer()

# file_name = sys.argv[1]
file_name = 'data/for-test/test.txt'

with open(file_name, 'rb') as inf:
    i = 0
    for line in inf:
        i += 1
        writer.add_document(title='line' + str(i), path='/a', content=line.decode('gbk', 'ignore'))
writer.commit()

searcher = ix.searcher()
parser = QueryParser('content', schema=ix.schema)

for keyword in ('水果小姐', '你', 'first', '中文', '交换机', '交换'):
    print('result of ' + keyword)
    q = parser.parse(keyword)
    results = searcher.search(q)
    for hit in results:
        print(hit.highlights('content'))
    print('=' * 10)
