from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

from src.api.handlers import router as img_router
from src.conf.settings import app_version

app = FastAPI(version=app_version)
app.include_router(router=img_router, prefix="/img")


@app.get("/")
def root(request: Request):
    return RedirectResponse(url="/docs", status_code=307)
