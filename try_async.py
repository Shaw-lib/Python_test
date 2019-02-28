"""
简单使用Python多进程多线程的例子
原po：http://github.com/denglj/aiotutorial
"""

import socket
from concurrent import futures


def blocking_way():
    sock = socket.socket()

    sock.connect(("baidu.com", 80))
    request = "GET / HTTP/1.0\r\nHost: baidu.com\r\n\r\n"
    sock.send(request.encode("ascii"))
    response = b""
    chunk = sock.recv(4096)
    while chunk:
        response += chunk

        chunk = sock.recv(4096)
    return response


def sync_way(n=10):
    # 同步方式
    res = []
    for i in range(n):
        res.append(blocking_way())
    return "request baidu.com {} times ".format(len(res))


def multiprocessing_way(n=10):
    # 多进程
    workers = n
    with futures.ProcessPoolExecutor(workers) as executor:
        futs = {executor.submit(blocking_way) for i in range(n)}
    return "request baidu.com {} times ".format(len([fut.result() for fut in futs]))


def multithreading_way(n=10):
    # 多进程切换开销大，多线程更加轻量，支持任务数量也更多
    workers = n
    with futures.ThreadPoolExecutor(workers) as executor:
        futs = {executor.submit(blocking_way) for i in range(n)}
    return "request baidu.com {} times ".format(len([fut.result() for fut in futs]))


# TODO 竞态处理：锁、同步队列

if __name__ == "__main__":
    import time

    # Test sync
    start = time.time()
    print(sync_way(20))
    print("sync: {} elapsed.".format(time.time() - start))

    # Test multiprocessing
    start = time.time()
    print(multiprocessing_way(20))
    print("multiprocessing_way: {} elapsed.".format(time.time() - start))

    # Test multithreading
    start = time.time()
    print(multithreading_way(20))
    print("multithreading_way: {} elapsed.".format(time.time() - start))

    ######RESULT######
    """
    request baidu.com 20 times 
    
    sync: 1.593940258026123 elapsed.
    multiprocessing_way: 0.6771807670593262 elapsed.
    multithreading_way: 0.10973215103149414 elapsed.
    """
