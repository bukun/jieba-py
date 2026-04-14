# -*- coding: UTF-8 -*-
import os
import sys

sys.path.append('.')

from whoosh.fields import *
from whoosh.index import open_dir
from whoosh.qparser import QueryParser

from wrapper.analyzer import ChineseAnalyzer

analyzer = ChineseAnalyzer()

schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored=True, analyzer=analyzer))
if not os.path.exists('tmp'):
    os.mkdir('tmp')
ix = open_dir('tmp')

searcher = ix.searcher()
parser = QueryParser('content', schema=ix.schema)

for keyword in ('水果小姐', '你', 'first', '中文', '交换机', '交换', '少林', '乔峰'):
    print('result of ', keyword)
    q = parser.parse(keyword)
    results = searcher.search(q)
    for hit in results:
        print(hit.highlights('content'))
    print('=' * 10)
