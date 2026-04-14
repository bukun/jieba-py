import re

# From jieba/__init__.py
re_userdict = re.compile(r'^(.+?)( [0-9]+)?( [a-z]+)?$', re.U)
re_eng_default = re.compile(r'[a-zA-Z0-9]', re.U)
re_han_default = re.compile(r'([\u4E00-\u9FD5a-zA-Z0-9+#&\._%\-]+)', re.U)
re_skip_default = re.compile(r'(\r\n|\s)', re.U)

# From jieba/finalseg.py
re_han_final = re.compile(r'([\u4E00-\u9FD5]+)')
re_skip_final = re.compile(r'([a-zA-Z0-9]+(?:\.\d+)?%?)')

# From jieba/posseg.py
re_han_detail = re.compile(r'([\u4E00-\u9FD5]+)')
re_skip_detail = re.compile(r'([\.0-9]+|[a-zA-Z0-9]+)')
re_han_internal = re.compile(r'([\u4E00-\u9FD5a-zA-Z0-9+#&\._]+)')
re_skip_internal = re.compile(r'(\r\n|\s)')
re_eng_pos = re.compile(r'[a-zA-Z0-9]+')
re_num_pos = re.compile(r'[\.0-9]+')
re_eng1_pos = re.compile(r'^[a-zA-Z0-9]$', re.U)
