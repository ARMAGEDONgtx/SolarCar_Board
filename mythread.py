import threading

class StoppableThread(threading.Thread):

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(StoppableThread, self).__init__(group=group, target=target,
			              name=name)
        self._stop_event = threading.Event()
        self._pause_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def pause(self):
        self._pause_event.set()

    def unpause(self):
        self._pause_event.clear()

    def paused(self):
        return self._pause_event.is_set()