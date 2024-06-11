from collections import deque
from select import select
from socket import AF_INET, SO_REUSEADDR, SOCK_STREAM, SOL_SOCKET, socket
from typing import Callable, Deque, Dict, Generator, Literal, NoReturn, Tuple

# Очередь задач
tasks: Deque[Generator[Tuple[str, socket], None, None]] = deque()
# Словари ожидания
recv_wait: Dict[socket, Generator[Tuple[str, socket], None, None]] = {}
send_wait: Dict[socket, Generator[Tuple[str, socket], None, None]] = {}


def run() -> None:
    while any([tasks, recv_wait, send_wait]):
        while not tasks:
            can_recv, can_send, _ = select(recv_wait, send_wait, [])
            for s in can_recv:
                tasks.append(recv_wait.pop(s))
            for s in can_send:
                tasks.append(send_wait.pop(s))
        task: Generator[Tuple[str, socket], None, None] = tasks.popleft()
        try:
            reason, resource = task.send(None)
            if reason == "recv":
                recv_wait[resource] = task
            elif reason == "send":
                send_wait[resource] = task
            else:
                raise RuntimeError("Unknown reason %r" % reason)
        except StopIteration:
            print("Task done")


def tcp_server(
    address: Tuple[str, int],
    handler: Callable[
        [socket, Tuple[str, int]], Generator[Tuple[str, socket], None, None]
    ],
) -> Generator[Tuple[str, socket], None, NoReturn]:
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        yield "recv", sock
        client, addr = sock.accept()
        tasks.append(handler(client, addr))


def echo_handler(
    client: socket, address: Tuple[str, int]
) -> Generator[Tuple[Literal["recv", "send"], socket], None, None]:
    print("Connection from", address)
    while True:
        yield "recv", client
        data: bytes = client.recv(1000)
        if not data:
            break
        yield "send", client
        client.send(b"GOT:" + data)
    print("Connection closed")


if __name__ == "__main__":
    tasks.append(tcp_server(("", 25000), echo_handler))
    run()
