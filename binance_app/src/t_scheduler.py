import sched
import time
import threading
from binance_app.main import main


class SchedulerClass():
    def __init__(self):
        self.i = 0
        self._lock = threading.Lock()

    def locked_request(self):
        print("self.i = ", self.i, end=" ")
        self.i += 1
        # one_day_seconds = 86400 
        seconds = 3.0 + time.time()
        request_plan = sched.scheduler(time.time, time.sleep)
        request_plan.enterabs(time=seconds, priority=1, action=main, argument=({"trading pair": None},))
        request_plan.run()
    
    def test_thr(self):
        
        self.locked_request()
        self._lock.release()


def t1():
    sc = SchedulerClass()
    while(True):
        sc._lock.acquire(timeout=4.0)
        x = threading.Thread(target=sc.test_thr)
        x.start()


def t0():
    x = threading.Thread(target=t1)
    x.start()
