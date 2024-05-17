# sample.py

from e71_logcall import logged


@logged
def add(x, y):
    return x + y


@logged
def sub(x, y):
    return x - y


add(3, 4)
