# coding: utf8

"""
    automagically
    ~~~~~~~~~~~~~~

"""

from functools import wraps
from byteplay import Code, opmap

__all__ = ['automagically']

LOAD_FAST = opmap['LOAD_FAST'] 
LOAD_GLOBAL = opmap['LOAD_GLOBAL'] 

def automagically(func):
    @wraps(func)
    def outer(f):
        @wraps(f)
        def inner(*args, **kws):
            injected = func()
            code = Code.from_code(f.func_code)
            code.args = tuple(injected.keys() + list(code.args))
            code.code = [(LOAD_FAST if (arg in injected and op == LOAD_GLOBAL) else op, arg) for op, arg in code.code]
            f.func_code = code.to_code()
            kws.update(injected)
            return f(*args, **kws)
        return inner
    return outer
