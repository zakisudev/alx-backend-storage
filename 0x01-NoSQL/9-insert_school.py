#!/usr/bin/env python3
""" Insert a document in Python """


def insert_school(mongo_collection, **kwargs):
    '''
    Write a Python function that inserts a new document
    '''
    return mongo_collection.insert(kwargs)
