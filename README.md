#py.evil

Collection of evil, what the fuck inducing tricks and other general badness

## module.py

A context manager that manipulates the calling module's globals to add everything that was not
previously in the global scope or begins with an underscore. You can include names that previously
existed in the global scope by including the names in the constructor of `module`.

For an example, do `from evil.test_module import *` and then examine the new scope, it'll include
`Derper`, `x`, and `will_import` but not `_secret` or `module`. Or, `from evil import test_module` and examine
`__all__` and notice that it does not include `_secret` or `module` in it (and that it also exists)
