#!/usr/bin/env python3
""" Cache class for storing data in Redis """
import redis
import uuid


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str or bytes or int or float) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
