import typer
from pathlib import Path

# local imports
from detapack import main

APP_NAME = main.APP_NAME
APP_VERSION = main.APP_VERSION

def get_app_dir():
    app_dir = typer.get_app_dir(APP_NAME)
    config_path: Path = Path(app_dir) / "config.json"
    templates_path: Path = Path(app_dir) / "templates.json"
    return Path(app_dir), config_path, templates_path