import inspect


__all__ = ['module']


def _get_caller_globals(frames=2):
    return inspect.stack()[frames][0].f_globals


class module:
    def __init__(self, *will_include):
        self._preexisting = _get_caller_globals().keys() - set(will_include)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        # reraise exception
        if exc_type:
            return None

        globs = _get_caller_globals()
        new = set(globs) - self._preexisting
        globs['__all__'] = tuple(x for x in new if not x.startswith('_'))
