#!/usr/bin/env python3
""" Cache class for storing data in Redis """
import redis
import uuid
import functools
from functools import wraps


def call_history(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))
        return result
    return wrapper


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def count_calls(method):
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            self._redis.incr(f"{method.__qualname__}:count")
            return method(self, *args, **kwargs)
        return wrapper

    @count_calls
    @call_history
    def store(self, data: str or bytes or int or float) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: callable = None):
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        return self.get(key, fn=str)

    def replay(method):
        self = method.__self__
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        inputs = self._redis.lrange(input_key, 0, -1)
        outputs = self._redis.lrange(output_key, 0, -1)
        print(f"{self.__qualname__} was called {len(inputs)} times:")
        for inp, out in zip(inputs, outputs):
            print(f"{self.__qualname__}(*{inp.decode('utf-8')}) ->
                  {out.decode('utf-8')}")
