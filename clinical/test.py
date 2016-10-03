# !/usr/bin/env python
# -*- coding: utf-8 -*-

# word2vec train
# This code is available under the MIT License.
# (c)2016 Jingwen Wang @ UML

'''
usage: python test.py keyword
'''

import gensim

model = gensim.models.Word2Vec.load_word2vec_format("trial.en.text.vector", binary=False)

list = model.most_similar("pain")

print list