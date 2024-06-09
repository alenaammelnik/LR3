import functools

def once(func):
    _cache = ''

    @functools.wraps(func)
    def inner(*args, **kwargs):
        nonlocal _cache
        from datetime import datetime
        if not inner.called:
            func(*args, **kwargs)
            _cache = str(datetime.now())
            inner.called = True

    inner.cache = _cache
    inner.called = False
    return inner

@once
def initialize_settings():
    print("Settings initialized.")

initialize_settings()
print(initialize_settings.cache)