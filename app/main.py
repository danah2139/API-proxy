from fastapi import FastAPI
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi import _rate_limit_exceeded_handler, Limiter
from slowapi.util import get_remote_address
from fastapi_cache import caches
from fastapi_cache.backends.memory import InMemoryCacheBackend, CACHE_KEY
from .routers import login
from .routers import register
from .routers import unknown
from .routers import users

app = FastAPI()
limiter = Limiter(key_func=get_remote_address, default_limits=["10/minute", "1000/day"])
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)
app.include_router(users.router)
app.include_router(unknown.router)
app.include_router(register.router)
app.include_router(login.router)


@app.on_event("startup")
async def startup():
    mc = InMemoryCacheBackend()
    caches.set(CACHE_KEY, mc)
    
@app.get("/")
async def test():
    return {"msg": "server starting"}
