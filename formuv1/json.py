#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 01:17:46 2020

@author: vanderneto
"""

import json

with open('media/dataset.json') as json_file:
    data = json.load(json_file)
    data {'datasetVersion': {'metadataBlocks': {'citation': {'fields': [{'value': titleform, 'typeClass': 'primitive', 'multiple': False, 'typeName': 'title'}, {'value': [{'authorName': {'value': '', 'typeClass': 'primitive', 'multiple': False, 'typeName': 'authorName'}, 'authorAffiliation': {'value': '', 'typeClass': 'primitive', 'multiple': False, 'typeName': 'authorAffiliation'}}], 'typeClass': 'compound', 'multiple': True, 'typeName': 'author'}, {'value': [{'datasetContactEmail': {'typeClass': 'primitive', 'multiple': False, 'typeName': 'datasetContactEmail', 'value': ''}, 'datasetContactName': {'typeClass': 'primitive', 'multiple': False, 'typeName': 'datasetContactName', 'value': ''}}], 'typeClass': 'compound', 'multiple': True, 'typeName': 'datasetContact'}, {'value': [{'dsDescriptionValue': {'value': '', 'multiple': False, 'typeClass': 'primitive', 'typeName': 'dsDescriptionValue'}}], 'typeClass': 'compound', 'multiple': True, 'typeName': 'dsDescription'}, {'value': [''], 'typeClass': 'controlledVocabulary', 'multiple': True, 'typeName': 'subject'}], 'displayName': 'Citation Metadata'}}}}
    print(data)