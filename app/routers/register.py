from fastapi import APIRouter, Request, Response
import requests
from .config import API_BASEURL


router = APIRouter(prefix="/api/register",)


@router.post("/", tags=["register"])
async def register(request: Request, response: Response):
    """
    wrapper for reqres register functionality

    - **request (Request)**: required for fastapi
    - **response (Response)**: required for fastapi
    - **returns: dic[str]**: response from post request to reqres remote server
    """
    headers = {"Content-Type": "application/json; charset=utf-8"}
    body = await request.body()
    res = requests.post(url=API_BASEURL + router.prefix, data=body, headers=headers)
    response.status_code = res.status_code
    return res.json()
