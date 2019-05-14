import time


def log(*args, **kwargs):
    dt = format_time(time.time())
    with open('log.txt', 'a', encoding='utf-8') as f:
        print(dt, *args, file=f, **kwargs)

def format_time(ct = 0):
    format = '%H:%M:%S'
    value = time.localtime(int(ct))
    return time.strftime(format,value)