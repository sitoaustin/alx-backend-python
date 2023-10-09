#!/usr/bin/env python3
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''spans wait_random n times
    '''
    newList = []
    for _ in n:
        newList.append(wait_random(max_delay))
