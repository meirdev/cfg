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
