#!/usr/bin/env python3

"""async routine called wait_n that takes in 2 int arguments
 (in this order): n and max_delay"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """calls coroutine and returns sorted list"""
    delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
