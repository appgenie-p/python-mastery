# e85_multitask.py

from collections import deque
from typing import Generator


def count_down(n: int) -> Generator[int, None, None]:
    while n > 0:
        yield n
        n -= 1


def count_up(n: int) -> Generator[int, None, None]:
    x = 0
    while x < n:
        yield x
        x += 1


def main() -> list[int]:
    cd = count_down(5)
    cu = count_up(5)

    tasks = deque()
    tasks.extend((cd, cu))

    results = []
    while tasks:
        fv = tasks.popleft()
        try:
            res = next(fv)
        except StopIteration:
            pass
        else:
            print(res)
            results.append(res)
            tasks.append(fv)
    return results


def up_and_down(n):
    yield from count_up(n)
    yield from count_down(n)


if __name__ == "__main__":
    for x in up_and_down(5):
        print(x)
