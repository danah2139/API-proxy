from fastapi import APIRouter, Request, Response, BackgroundTasks, Depends
from fastapi_cache.backends.memory import InMemoryCacheBackend
from .config import API_BASEURL, set_in_cache_get_request, memory_cache


router = APIRouter(prefix="/api/unknown",)


@router.get("/", tags=["unknown"])
async def read_unknowns(request: Request, response: Response, background_tasks: BackgroundTasks, page: int = 0, delay: int = 0, 
                        cache: InMemoryCacheBackend = Depends(memory_cache)):
    """
    wrapper for reqres read all unknowns functionality
    """

    url = f'{API_BASEURL}{router.prefix}?delay={delay}&page={page}'
    in_cache = await cache.get(url)
    if not in_cache:
        background_tasks.add_task(set_in_cache_get_request, url, cache)
    return {'response': in_cache or 'panding'}



@router.get("/{user_id}", tags=["unknown"])
async def read_unknown(request: Request, response: Response, background_tasks: BackgroundTasks, user_id: int, page: int = 0, delay: int = 0, 
                        cache: InMemoryCacheBackend = Depends(memory_cache)):
    url = f'{API_BASEURL}/{user_id}{router.prefix}?delay={delay}&page={page}'
    in_cache=await cache.get(url)
    if not in_cache:
        background_tasks.add_task(set_in_cache_get_request, url, cache)
    return {'response': in_cache or 'panding'}
