import uvicorn

from src.conf import Config

uvicorn.run(
    "src.api_v1.main:app",
    host=Config.app_host,
    port=Config.app_port,
    workers=Config.app_workers_count,
    reload=Config.development,
)
