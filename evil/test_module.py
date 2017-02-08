from .module import module

will_import = 1

with module('will_import'):
    x = 3

    class Derper:
        pass

    _secret = 1
