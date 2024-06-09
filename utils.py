import functools
import json

def memoized(func):
    cache = {}

    @functools.wraps(func)
    def inner(*args, **kwargs):
        key = (args, func.__name__, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    inner.cache = cache
    return inner

def save_cache(cache):
    with open('cache.json', 'w') as f:
        json.dump(cache, f)

def load_cache():
    with open('cache.json', 'r') as f:
        return json.load(f)

@memoized
def factorial1(n):
    from math import factorial
    return factorial(n)

@memoized
def foo(a, **kwargs):
    return 'Hey!'

