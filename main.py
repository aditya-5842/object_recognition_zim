import uvicorn

from settings import settings


def main() -> None:
    """Entrypoint of the application."""
    uvicorn.run(
        "app:app",
        workers=settings.workers_count,
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
        log_level=settings.log_level.value.lower(),
    )


if __name__ == "__main__":
    main()
