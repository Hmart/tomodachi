import asyncio
from typing import Generator

import pytest


@pytest.fixture(scope="module")
def loop() -> Generator:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    yield loop

    try:
        if loop and not loop.is_closed():
            loop.close()
        loop = asyncio.get_event_loop()
        if loop and not loop.is_closed():
            loop.close()
    except RuntimeWarning:
        pass
    except RuntimeError:
        pass
