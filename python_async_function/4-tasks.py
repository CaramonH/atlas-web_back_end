#!/usr/bin/env python3

"""Take wait_n and alter it into task_wait_n."""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """calls coroutine and returns sorted list"""
    delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
