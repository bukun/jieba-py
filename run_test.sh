set -e
python3 test/demo.py
python3 test/extract_tags_idfpath.py test/test.txt
python3 test/extract_tags.py test/test.txt
python3 test/extract_tags_stop_words.py test/test.txt
python3 test/extract_tags_with_weight.py test/test.txt
python3 test/extract_topic.py test
python3 test/jieba_test.py
python3 test/test_base.py
python3 test/test_bug.py
python3 test/test_change_dictpath.py
python3 test/test_cutall.py
python3 test/test_cut_for_search.py
python3 test/test_file.py
python3 test/test_lock.py
python3 test/test_multithread.py
python3 test/test_no_hmm.py
python3 test/test_pos_file.py
python3 test/test_pos_no_hmm.py
python3 test/test_pos.py
python3 test/test_tokenize_no_hmm.py
python3 test/test_tokenize.py
python3 test/test_userdict.py
python3 test/test_whoosh_file.py
python3 test/test_whoosh_file_read.py
python3 test/test_whoosh.py
