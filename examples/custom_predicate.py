import shutil

from cfg import *


class AppExists:
    def __init__(self, app: str) -> None:
        self._app = app

    def __bool__(self) -> bool:
        return shutil.which(self._app) is not None


app_exists = AppExists


def copy(src, dst):
    print(f"cp {src} {dst}")


@cfg(app_exists("scp"))  # type: ignore[no-redef]
def copy(src, dst):
    print(f"scp {src} {dst}")


@cfg(app_exists("rsync"))  # type: ignore[no-redef]
def copy(src, dst):
    print(f"rsync {src} {dst}")


copy("/file", "/new_path/file")
