from fastapi import APIRouter, Request, Response, BackgroundTasks, Depends
from fastapi_cache.backends.memory import InMemoryCacheBackend
from .config import API_BASEURL, get_response_from_cache, memory_cache


router = APIRouter(prefix="/api/unknown",)


@router.get("/", tags=["unknown"])
async def read_unknowns(request: Request, response: Response, background_tasks: BackgroundTasks, page: int = 0, delay: int = 0, 
                        cache: InMemoryCacheBackend = Depends(memory_cache)):
    """
    wrapper for reqres read all unknowns functionality
    """

    url = f'{API_BASEURL}{router.prefix}?delay={delay}&page={page}'
    return await get_response_from_cache(url, cache, background_tasks)




@router.get("/{user_id}", tags=["unknown"])
async def read_unknown(request: Request, response: Response, background_tasks: BackgroundTasks, user_id: int, page: int = 0, delay: int = 0, 
                        cache: InMemoryCacheBackend = Depends(memory_cache)):
    url = f'{API_BASEURL}/{user_id}{router.prefix}?delay={delay}&page={page}'
    return await get_response_from_cache(url, cache, background_tasks)
