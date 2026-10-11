import logging
from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel

from app.config import Settings


class HealthResponse(BaseModel):
    status: Literal["ok"]
    app_name: str


def create_app(settings: Settings | None = None) -> FastAPI:
    """Create an application with validated settings."""
    config = settings if settings is not None else Settings()

    logging.basicConfig(level=config.log_level)

    application = FastAPI(
        title=config.app_name,
        version="0.1.0",
    )

    @application.get("/health", response_model=HealthResponse)
    def health() -> HealthResponse:
        return HealthResponse(
            status="ok",
            app_name=config.app_name,
        )

    return application


app = create_app()