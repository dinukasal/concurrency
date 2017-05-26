# -*- coding: utf-8 -*-
"""
Created on Wed May 24 21:26:28 2017

@author: dinuka
"""

import threading
import time

def thread1(lock):
    for i in range(5):
        lock.acquire()
        try:
            print 'A',
        finally:
            lock.release()
        time.sleep(0.1)
        
def thread2(lock):
    for i in range(5):
        lock.acquire()
        try:
            print 'B',
        finally:
            lock.release()
        time.sleep(0.1)

lock = threading.Lock()
w = threading.Thread(target=worker_with, args=(lock,))
nw = threading.Thread(target=worker_no_with, args=(lock,))

w.start()
nw.start()