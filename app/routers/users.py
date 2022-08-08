from fastapi import APIRouter, Request, Response
import requests
from fastapi_cache.decorator import cache
from .config import API_BASEURL


router = APIRouter(prefix="/api/users",)


@router.get("/", tags=["users"])
@cache(expire=60)
async def read_users(request: Request, response: Response, page: int = 0, delay: int = 0):
    res = requests.get(f'{API_BASEURL}{router.prefix}?delay={delay}&page={page}')
    response.status_code = res.status_code
    return res.json()


@router.get("/{user_id}", tags=["users"])
@cache(expire=60)
async def read_user(request: Request, response: Response, user_id: int, page: int = 0, delay: int = 0):
    res = requests.get(f'{API_BASEURL}{router.prefix}/{user_id}?delay={delay}&page={page}')
    response.status_code = res.status_code
    return res.json()


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
