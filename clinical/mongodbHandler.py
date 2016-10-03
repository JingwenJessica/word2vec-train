#!/usr/bin/env python
# -*- coding: utf-8 -*-

# kuaiwenbao copy system category classification train
# This code is available under the MIT License.
# (c)2016 Jingwen Wang @ UML



import pymongo
from pymongo import MongoClient

import normalization


class mongodbHandler:
    def __init__(self):
        """
        Initial function
        :param
        """
        self.ip = "129.63.16.51"  # ip mongodb
        self.port = 27017  # port mongodb

    def trial2TextList(self, trial):
        textList = []

        if "brief_title" in trial:
            text = normalization.normalization( trial["brief_title"] )
            textList.append( text )

        if "official_title" in trial:
            if trial["official_title"] != trial["brief_title"]:
                text = normalization.normalization(trial["official_title"])
                textList.append(text)

        if "study_design" in trial:
            text = normalization.normalization(trial["study_design"])
            textList.append(text)

        if "brief_summary" in trial:
            text = normalization.normalization(trial["brief_summary"]["textblock"])
            textList.append(text)

        return textList

    def loadTrainTextByPage(self, pageId, pageSize):
        '''
        Load clinical trials by page id
        :param pageId: page id start from 1
        :param pageSize: trials per page
        :return:
        '''
        if pageId < 1 :
            pageId = 1;

        skip = (pageId - 1) * pageSize

        trialDB = "ClinicalTrials"  # db mongodb
        trialColl = "clinicalTrialsGov"  # copy systems collection name mongodb

        trialsList = list()

        conn = pymongo.MongoClient(self.ip, self.port)  # get data from tencent server
        try:
            db = conn[trialDB]
            coll = db[trialColl]
            cursor = coll.find().sort("_id", -1).skip(skip).limit(pageSize)

            for document in cursor:
                del document["_id"]
                textList = self.trial2TextList( document )
                trialsList.append( textList )

        except Exception, ex:
            print ex.message
        conn.close()
        return trialsList




