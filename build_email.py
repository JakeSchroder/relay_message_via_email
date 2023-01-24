from rq import Queue
from redis import Redis
from send_email import send_message

def build_email():
    q = Queue(connection=Redis())
    q.enqueue(send_message(data))
