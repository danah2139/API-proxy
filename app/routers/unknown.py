from fastapi import APIRouter, Request, Response
import requests
from fastapi_cache.decorator import cache
from .config import API_BASEURL


router = APIRouter(prefix="/api/unknown",)


@router.get("/", tags=["unknown"])
@cache(expire=60)
async def read_unknowns(request: Request, response: Response, page: int = 0, delay: int = 0):
    """
    wrapper for reqres read all unknowns functionality
    """

    res = requests.get(f'{API_BASEURL}{router.prefix}?delay={delay}&page={page}')
    response.status_code = res.status_code
    return res.json()


@router.get("/{user_id}", tags=["unknown"])
@cache(expire=60)
async def read_unknown(request: Request, response: Response, user_id: int, page: int = 0, delay: int = 0):
    res = requests.get(f'{API_BASEURL}/{user_id}{router.prefix}?delay={delay}&page={page}')
    response.status_code = res.status_code
    return res.json()
