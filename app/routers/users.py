from fastapi import APIRouter, Request, Response, BackgroundTasks, Depends
from fastapi_cache.backends.memory import InMemoryCacheBackend
import requests
from .config import API_BASEURL, get_response_from_cache, memory_cache


router = APIRouter(prefix="/api/users",)
    
@router.get("/", tags=["users"])
async def read_users(request: Request, response: Response, background_tasks: BackgroundTasks,page: int = 0, delay: int = 0,
                    cache: InMemoryCacheBackend = Depends(memory_cache)):
    """
        wrapper for reqres read all users functionality

        :param request (Request): default  for fastapi
        :param response (Response): default  for fastapi
        :param background_tasks (BackgroundTasks): background tasks for running operations after returning a response
        :param page (int, optional): query argument for pagination. Defaults to 0.
        :param delay (int, optional):query argument. Defaults to 0.
        :param cache (InMemoryCacheBackend, optional): in memory cache. Defaults to Depends(memory_cache).
        :returns:  dic[str]: response from the cache OR 'pending'
    """    
    url = f'{API_BASEURL}{router.prefix}?delay={delay}&page={page}'
    return await get_response_from_cache(url, cache, background_tasks)


@router.get("/{user_id}", tags=["users"])
async def read_user(request: Request, response: Response, background_tasks: BackgroundTasks, user_id: int, page: int = 0, delay: int = 0,
                    cache: InMemoryCacheBackend = Depends(memory_cache)):
    """
        wrapper for reqres read user functionality

        :param request (Request): default  for fastapi
        :param response (Response): default  for fastapi
        :param background_tasks (BackgroundTasks): background tasks for running operations after returning a response
        :param user_id (int): user id param from client request
        :param page (int, optional): query argument for pagination. Defaults to 0.
        :param delay (int, optional):query argument. Defaults to 0.
        :param cache (InMemoryCacheBackend, optional): in memory cache. Defaults to Depends(memory_cache).
        :returns:  dic[str]: response from the cache OR 'pending'
    """
    url = f'{API_BASEURL}{router.prefix}/{user_id}?delay={delay}&page={page}'
    return await get_response_from_cache(url, cache, background_tasks)


@router.post("/", tags=["users"])
async def create_users(request: Request, response: Response):
    """
        wrapper for reqres create user functionality
        
        :param request (Request): default for fastapi
        :param response (Response): default for fastapi
        :returns: dic[str]: response from post request to reqres remote server
    """    
    headers = {"Content-Type": "application/json; charset=utf-8"}
    body = await request.body()
    res = requests.post(url=API_BASEURL + router.prefix, data=body, headers=headers)
    response.status_code = res.status_code
    return res.json()


@router.put("/{user_id}", tags=["users"])
async def update_users(request: Request, response: Response, user_id: int):
    """
        wrapper for reqres update user functionality

        :param request (Request): default for fastapi
        :param response (Response): default for fastapi
        :param user_id (int): user id param from client request
        :returns: dic[str]: response from put request to reqres remote server
    """
    headers = {"Content-Type": "application/json; charset=utf-8"}
    body = await request.body()
    res = requests.put(url=f'{API_BASEURL}{router.prefix}/{user_id}', data=body, headers=headers)
    response.status_code = res.status_code
    return res.json()


@router.patch("/{user_id}", tags=["users"])
async def patch_users(request: Request, response: Response, user_id: int):
    """
        wrapper for reqres patch user functionality

        :param request (Request): default for fastapi
        :param response (Response): default for fastapi
        :param user_id (int): user id param from client request
        :returns: dic[str]: response from patch request to reqres remote server
    """
    headers = {"Content-Type": "application/json; charset=utf-8"}
    body = await request.body()
    res = requests.patch(url=f'{API_BASEURL}{router.prefix}/{user_id}', data=body, headers=headers)
    response.status_code = res.status_code
    return res.json()


@router.delete("/{user_id}", tags=["users"])
async def delete_users(request: Request, response: Response, user_id: int):
    """
        wrapper for reqres delete user functionality

        :param request (Request): default for fastapi
        :param response (Response): default for fastapi
        :param user_id (int): user id param from client request
        :returns: dic[str]: status from delete user request reqres remote server
    """
    res = requests.delete(f'{API_BASEURL}{router.prefix}/{user_id}')
    response.status_code = res.status_code
    return res
