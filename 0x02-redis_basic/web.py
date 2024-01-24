#!/usr/bin/env python3
""" Web page get and post """
import requests
import redis
import functools
r = redis.Redis()


def count_url_calls(func):
    @functools.wraps(func)
    def wrapper(url):
        r.incr(f"count:{url}")
        return func(url)
    return wrapper


@count_url_calls
def cache_page(func):
    @functools.wraps(func)
    def wrapper(url):
        result = r.get(url)
        if result is None:
            result = func(url)
            r.set(url, result, ex=10)
        return result
    return wrapper


@cache_page
def get_page(url: str) -> str:
    response = requests.get(url)
    return response.text
