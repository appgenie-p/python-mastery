from e52 import parse_line, worker


def test_worker_returns_sum_after_5_sec():
    sut = worker(5, 4)

    assert sut == 9


def test_worker_in_thread():
    import threading

    t = threading.Thread(target=worker, args=(2, 3))
    t.start()
