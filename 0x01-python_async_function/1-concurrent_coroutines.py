#!/usr/bin/env python3
import wait_random
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''spans wait_random n times
    '''
    newList = []
    for _ in n:
        newList.append(wait_random(max_delay))
