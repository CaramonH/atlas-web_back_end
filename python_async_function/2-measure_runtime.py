#!/usr/bin/env python3

"""Function measure_time with integers n and max_delay as arguments that
measures the total execution time for wait_n(n, max_delay), and returns
total_time / n"""
import asyncio
from time import perf_counter
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int = 10) -> float:
    """Measures the total execution time for wait_n
    and returns the average time per operation."""
    start_time = perf_counter()
    await wait_n(n, max_delay)
    end_time = perf_counter()
    total_time = end_time - start_time
    return total_time / n
