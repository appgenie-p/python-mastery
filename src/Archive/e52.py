import time
from concurrent.futures import Future
from typing import Optional


def worker(x, y):
    print("About to work")
    time.sleep(5)
    print("Done")
    return x + y


def parse_line(line: str) -> Optional[tuple]:
    res = tuple(line.split("="))
    match res:
        case (x, y):
            return res
    return None


def do_work(x, y, fut: Future):
    fut.set_result(worker(x, y))


if __name__ == "__main__":
    from concurrent.futures import ThreadPoolExecutor
    pool = ThreadPoolExecutor()
    fut = pool.submit(worker, 2, 3)
    print(fut.result())
