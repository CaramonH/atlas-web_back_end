#!/usr/bin/env python3

"""Function measure_time with integers n and max_delay as arguments that
measures the total execution time for wait_n(n, max_delay), and returns
total_time / n"""
import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int = 10) -> float:
    """Measures the total execution time for wait_n
    and returns the average time per operation."""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return (end - start) / n
