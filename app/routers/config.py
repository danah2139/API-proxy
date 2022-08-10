from fastapi import BackgroundTasks
from fastapi_cache import caches
from fastapi_cache.backends.memory import InMemoryCacheBackend, CACHE_KEY
import requests


API_BASEURL = 'https://reqres.in'


def memory_cache():
    return caches.get(CACHE_KEY)

async def set_in_cache_get_request(url: str, cache: InMemoryCacheBackend, message="") -> None:
    res = requests.get(url)
    await cache.set(url, res.json())
    await cache.expire(url, 1000)
    

async def get_response_from_cache(url:str, cache: InMemoryCacheBackend, background_tasks: BackgroundTasks):
    in_cache = await cache.get(url)
    if not in_cache:
        background_tasks.add_task(set_in_cache_get_request ,url,cache)    
    return {'response': in_cache or 'pending'}
    
