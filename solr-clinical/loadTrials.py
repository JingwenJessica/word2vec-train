#!/usr/bin/env python
# -*- coding: utf-8 -*-

# word2vec train
# This code is available under the MIT License.
# (c)2016 Jingwen Wang @ UML

'''
usage: python loadTrials.py data/trials/trials.en.txt
'''

import logging
import os.path
import sys


import mongodbHandler

# from gensim.corpora import WikiCorpus


mongodbHandler = mongodbHandler.mongodbHandler()


if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments
    if len(sys.argv) < 2:
        print globals()['__doc__'] % locals()
        sys.exit(1)
    outp = sys.argv[1]
    space = " "
    i = 0

    outputFile = open(outp, 'w')

    pageId = 0
    pageSize = 1000
    while True:
        pageId += 1
        trialsList = mongodbHandler.loadTrainTextByPage(pageId, pageSize)
        if not trialsList:
            break
        for trial in trialsList:
            try:
                outputFile.write(space.join(trial) + "\n")
                i += 1
                if (i % 1000 == 0):
                    logger.info("Load " + str(i) + " trials")
            except:
                e = sys.exc_info()[0]
                # print( "[!] Error: %s" % e )
                # print trial
    outputFile.close()
    logger.info("Finished Load " + str(i) + " trials")