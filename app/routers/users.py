from fastapi import APIRouter, Request, Response, BackgroundTasks, Depends
from fastapi_cache.backends.memory import InMemoryCacheBackend
import requests
from .config import API_BASEURL, set_in_cache_get_request, memory_cache


router = APIRouter(prefix="/api/users",)
    
@router.get("/", tags=["users"])
async def read_users(request: Request, response: Response, background_tasks: BackgroundTasks, page: int = 0, delay: int = 0, 
                    cache: InMemoryCacheBackend = Depends(memory_cache)):
    url = f'{API_BASEURL}{router.prefix}?delay={delay}&page={page}'
    in_cache = await cache.get(url)
    if not in_cache:
        background_tasks.add_task(set_in_cache_get_request, url,cache)
    return {'response': in_cache or 'panding'}


@router.get("/{user_id}", tags=["users"])
async def read_user(request: Request, response: Response, background_tasks: BackgroundTasks, user_id: int, page: int = 0, delay: int = 0, 
                    cache: InMemoryCacheBackend = Depends(memory_cache)):
    url = f'{API_BASEURL}{router.prefix}/{user_id}?delay={delay}&page={page}'
    in_cache = await cache.get(url)
    if not in_cache:
        background_tasks.add_task(set_in_cache_get_request, url)
    return {'response': in_cache or 'panding'}


@router.post("/", tags=["users"])
async def create_users(request: Request, response: Response):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    body = await request.body()
    res = requests.post(url=API_BASEURL + router.prefix, data=body, headers=headers)
    response.status_code = res.status_code
    return res.json()


@router.put("/{user_id}", tags=["users"])
async def update_users(request: Request, response: Response, user_id: int):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    body = await request.body()
    res = requests.put(url=f'{API_BASEURL}{router.prefix}/{user_id}', data=body, headers=headers)
    response.status_code = res.status_code
    return res.json()


@router.patch("/{user_id}", tags=["users"])
async def patch_users(request: Request, response: Response, user_id: int):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    body = await request.body()
    res = requests.patch(url=f'{API_BASEURL}{router.prefix}/{user_id}', data=body, headers=headers)
    response.status_code = res.status_code
    return res.json()


@router.delete("/{user_id}", tags=["users"])
async def delete_users(request: Request, response: Response, user_id: int):
    res = requests.delete(f'{API_BASEURL}{router.prefix}/{user_id}')
    response.status_code = res.status_code
    return res
