import enum
from pathlib import Path
from tempfile import gettempdir

from pydantic_settings import BaseSettings
from yarl import URL

TEMP_DIR = Path(gettempdir())


class LogLevel(str, enum.Enum):  # noqa: WPS600
    """Possible log levels."""

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class Settings(BaseSettings):
    """
    Application settings.

    These parameters can be configured
    with environment variables.
    """

    host: str = "127.0.0.1"
    port: int = 8080
    # quantity of workers for uvicorn
    workers_count: int = 1
    # Enable uvicorn reloading
    reload: bool = False

    log_level: LogLevel = LogLevel.INFO

    # camera calibration
    # front_camera_calibrated: bool = True
    # back_camera_calibrated: bool = True
    front_camera_position: str = ""
    back_camera_position: str = ""
    # save calibration path
    save_calibration_path: str = "cameraCalibration"
    save_calibration_suffix: str = "CameraConfig.json"

    # ml-model path
    ml_model_path: str = ""

    # camera credentials
    front_camera_ip: str = ""
    back_camera_ip: str = ""

    front_camera_port: str = ""
    back_camera_port: str = ""

    front_camera_user: str = ""
    back_camera_user: str = ""

    front_camera_password: str = ""
    back_camera_password: str = ""

    # image path for local-development
    back_camera_image_path: str = "data/backCamera/backLeft/00168858_20230403_0755_2_2.jpg"
    front_camera_image_path: str = "data/frontCamera/frontRight/00170608_20230426_1648_2_1.jpg"
    # back_camera_image_path: str = "data/backCamera/backRight/00170665_20230427_1208_1_2.jpg"
    # front_camera_image_path: str = "data/frontCamera/frontLeft/00168845_20230401_0841_2_1.jpg"

    class Config:
        env_file = ".env"
        env_prefix = "API_"
        env_file_encoding = "utf-8"


settings = Settings()
