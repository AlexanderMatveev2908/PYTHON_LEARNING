import threading
from time import sleep
from typing import Callable


class Interval:
    def __init__(self, cb: Callable[..., None], sec: float):
        self.cb = cb
        self.sec = sec
        self._stopped = False
        self._timer = None

    def _wrap(self):
        if self._stopped:
            return

        self.cb()
        self._schedule()

    def _schedule(self):
        self._timer = threading.Timer(self.sec, self._wrap)
        self._timer.daemon = True
        self._timer.start()

    def start(self):
        self._stopped = False
        self._schedule()

    def stop(self):
        self._stopped = True
        if self._timer:
            self._timer.cancel()


count = 0


def say_hi():
    global count
    count += 1
    print(count)
    if count >= 5:
        i.stop()
        for k, v in vars(i).items():
            print(k, v)
        print("Stopped interval.")


i = Interval(say_hi, 1)
i.start()


while True:
    sleep(1)
