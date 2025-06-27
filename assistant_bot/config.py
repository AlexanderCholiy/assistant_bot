import os
from typing import Optional, Union

from dotenv import load_dotenv

from .exceptions import EnvVarsErr, DirExistErr, FileExistErr


load_dotenv(override=True)


class Config:

    def _raise_if_missing(
        self,
        items: list[str],
        check_func: callable,
        error_cls: Union[DirExistErr, FileExistErr]
    ) -> None:
        missing = [item for item in items if not check_func(item)]
        if missing:
            raise error_cls(missing)

    def check_env_vars(
        self, env_vars: dict[str, Optional[str]]
    ):
        missing_vars = [name for name, val in env_vars.items() if val is None]
        if missing_vars:
            raise EnvVarsErr(missing_vars)

    def check_dirs(self, dirs: list[str]):
        self._raise_if_missing(dirs, os.path.isdir, DirExistErr)

    def check_files(self, files: list[str]):
        self._raise_if_missing(files, os.path.isfile, FileExistErr)


class AppConfig(Config):
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    DEBUG = os.getenv('DEBUG', 'False') == 'True'

    def __init__(self):
        super().__init__()
        env_vars = {
            'BOT_TOKEN': self.BOT_TOKEN,
        }
        self.check_env_vars(env_vars)


app_config = AppConfig()
