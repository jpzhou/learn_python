# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:
# Author:      jp $
# -------------------------------------------------------------------------------

import time
import functools
import threading


def async(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        my_thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        my_thread.start()
    return wrapper

@async
def foo(x, y):
    c = 0
    while c < 5:
        c = c + 1
    print x, y
    time.sleep(10)

foo(456, 789)
print 'start'
# foo(123, 345)
