#!/usr/bin/env python3

"""Coroutine called async_comprehension that takes no arguments.
    The coroutine will collect 10 random numbers with aync and return them."""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """coroutine that uses async comprehension to collect 10 random numbers"""
    return [i async for i in async_generator()]
