import sys

def foo(x):
    return x + x

sys.modules[__name__] = foo