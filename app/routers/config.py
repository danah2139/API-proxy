from fastapi import BackgroundTasks
from fastapi_cache import caches
from fastapi_cache.backends.memory import InMemoryCacheBackend, CACHE_KEY
import requests


API_BASEURL = 'https://reqres.in'


def memory_cache():
    """
    memory cache instance
    
        returns: BaseCacheBackend : memory cache instance
    """    
    return caches.get(CACHE_KEY)

async def set_in_cache_get_request(url: str, cache: InMemoryCacheBackend) -> None:
    """
    create get api requset and set the response in memory cache

        :param url (str): url from client 
        :param cache (InMemoryCacheBackend): memory cache
    """ 
    res = requests.get(url)
    await cache.set(url, res.json())
    await cache.expire(url, 1000)
    

async def get_response_from_cache(url:str, cache: InMemoryCacheBackend, background_tasks: BackgroundTasks):
    """
        get and return response from cache if exists 
        else than create get request and set in memory cache

        :param url (str): _description_
        :param cache (InMemoryCacheBackend): memory cache
        :param background_tasks (BackgroundTasks): background tasks for running operations after returning a response
        returns:dic[str]: response from cache or 'pending'
    """    
    in_cache = await cache.get(url)
    if not in_cache:
        background_tasks.add_task(set_in_cache_get_request ,url,cache)    
    return {'response': in_cache or 'pending'}
    
