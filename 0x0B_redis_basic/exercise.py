#!/usr/bin/env python3
"""Writing Strings to Redis.
Module which defines the cache class using Redis
"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """INCR a count for the key when the method is called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Store inputs and outputs for a function"""
    inputs_key = f"{method.__qualname__}:inputs"
    outputs_key = f"{method.__qualname__}:outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(inputs_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, str(result))
        return result

    return wrapper


class Cache:
    """Defines a Redis cache"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a random key and stores data in Redis"""
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> \
            Union[str, bytes, int, float]:
        """Retrieve a given key value from Redis"""
        value = self._redis.get(key)
        if value is not None and fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """Get a string from Redis"""
        value = self.get(key, str)
        return value

    def get_int(self, key: str) -> Optional[int]:
        """Get an int from Redis"""
        value = self.get(key, int)
        return value


def replay(method: Callable) -> None:
    """Display the history of calls for a function"""
    method_name = method.__qualname__
    count_key = method_name
    inputs_key = f"{method_name}:inputs"
    outputs_key = f"{method_name}:outputs"

    count = method.__self__._redis.get(count_key)
    inputs = method.__self__._redis.lrange(inputs_key, 0, -1)
    outputs = method.__elf__._redis.lrange(outputs_key, 0, -1)

    print(f"{method_name} was called {int(count)} times:")
    for input_str, output_str in zip(inputs, outputs):
        print(f"{method_name}(*{input_str.decode('utf-8')}) ->\
              {output_str.decode('utf-8')}")
