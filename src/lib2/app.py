import typing as t

import lib1.app


def add_args(args: t.List[int]) -> int:
    return lib1.app.add(*args)
