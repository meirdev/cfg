import os


class Windows:
    def __bool__(self) -> bool:
        return os.name == "nt"


windows = Windows()


class Unix:
    def __bool__(self) -> bool:
        return os.name == "posix"


unix = Unix()
