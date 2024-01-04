#!/usr/bin/env python3

"""Coroutine that loops 10x, each time waiting async 1 second,
    then yield a random number between 0 and 10."""
import asyncio
import random


async def async_generator():
    """loops 10x, async 1 second, yields random between 0-10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0,10)
