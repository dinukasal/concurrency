# -*- coding: utf-8 -*-
"""
Created on Wed May 24 21:26:28 2017

@author: dinuka
"""

import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def worker_with(lock):
    for i in range(5):
        #with lock:
        #    logging.debug('Lock acquired via with')
        lock.acquire()
        try:
            print 'A',
        finally:
            lock.release()
        time.sleep(0.1)
        
def worker_no_with(lock):
    for i in range(5):
        lock.acquire()
        try:
            logging.debug('Lock acquired directly')
            print 'B',
        finally:
            lock.release()
        time.sleep(0.1)

lock = threading.Lock()
w = threading.Thread(target=worker_with, args=(lock,))
nw = threading.Thread(target=worker_no_with, args=(lock,))

w.start()
nw.start()