from fastapi import FastAPI
from fastapi_limiter import FastAPILimiter

app = FastAPI()

from basedbin import endpoints
