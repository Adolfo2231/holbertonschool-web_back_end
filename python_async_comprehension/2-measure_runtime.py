#!/usr/bin/env python3
"""Module for measure_runtime coroutine.
This module provides a coroutine to measure the runtime
of running async_comprehension in parallel.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime of executing
    async_comprehension four times in parallel."""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return end - start
