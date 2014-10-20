import time

from redis import Redis
from rq import Queue

from posters.vancouver import craigslist


__author__ = 'sepehrtaheri'


def post(args):
    conn = Redis()

    print(conn)

    q = Queue(connection=conn)

    print(q)

    result = q.enqueue(craigslist.post, args)

    print("before sleep", result.result)
    print("before sleep", result.return_value)

    time.sleep(2)

    print("after sleep", result.result)
    print("after sleep", result.return_value)

    return result