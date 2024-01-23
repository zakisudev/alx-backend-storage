#!/usr/bin/env python3
""" Find a match with regex """

from pymongo import MongoClient


def main() -> None:
    """ Main function """
    client = MongoClient('mongodb://localhost:27017')
    db = client['my_db']
    collection = db['school']

    pipeline = [{'$match': {'name': {'$regex': '^Holberton'}}}]

    documents = collection.aggregate(pipeline)

    for document in documents:
        print(document)

    client.close()


if __name__ == '__main__':
    main()
