class Resource:
    class NotAvailableError(Exception):
        pass

    def __init__(self):
        self._resource = None

    def acquire(self, *a, **kw):
        raise NotImplementedError

    def release(self):
        raise NotImplementedError

    def open(self, *a, **kw):
        if self._resource is None:
            self._resource = self.acquire(*a, **kw)

        return self._resource

    def close(self):
        if self._resource is None:
            return

        self.release()
        self._resource = None

    def ensure_open(self, message="resource not available"):
        if self._resource is None:
            raise Resource.NotAvailableError(message)

    def __enter__(self):
        return self.open()

    def __exit__(self, type=None, value=None, traceback=None):
        # todo: does anything need to be done with the args?
        self.close()
