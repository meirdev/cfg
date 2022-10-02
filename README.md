# Conditional runtime

Add a conditional runtime in your script.

# Example

```python
from cfg import *


@cfg(unix)
def foo():
    print("Hello Unix!")


@cfg(windows)  # type: ignore[no-redef]
def foo():
    print("Hello Windows!")


@cfg(not any([unix, windows]))  # type: ignore[no-redef]
def foo():
    print("Hello Other!")


foo()

# In Windows: Hello Windows!
# In Unix: Hello Unix!
# Neither: Hello Other!
```

With custom predicate:

```python
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
```
