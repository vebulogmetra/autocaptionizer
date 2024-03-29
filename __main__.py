import uvicorn

from src.conf import config

uvicorn.run(
    "src.api_v1.main:app",
    host=config.app_host,
    port=config.app_port,
    reload=config.development,
)
