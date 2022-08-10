from fastapi_cache import caches
from fastapi_cache.backends.memory import InMemoryCacheBackend, CACHE_KEY
from fastapi import Depends
import requests


API_BASEURL = 'https://reqres.in'


def memory_cache():
    return caches.get(CACHE_KEY)


async def set_in_cache_get_request(url: str, message="", cache: InMemoryCacheBackend = Depends(memory_cache)) -> None:
    res = requests.get(url)
    await cache.set(url, res.json())
    await cache.expire(url, 1000)
    
# async def check_if_in_cache():
#     in_cache = await cache.get(url)
#     if not in_cache:
#         background_tasks.add_task(set_in_cache_get_request url)    
    
