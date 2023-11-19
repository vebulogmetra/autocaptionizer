from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

from src.api_v1.handlers import router as img_router
from src.conf import config

app = FastAPI(version=config.app_version)
app.include_router(router=img_router, prefix="/img")


@app.get("/")
def root(request: Request):
    return RedirectResponse(url="/docs", status_code=307)
