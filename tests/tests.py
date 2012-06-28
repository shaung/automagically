# coding: utf8

from automagically import *

def test_foo():
    @automagically
    def with_magic():
        return {'magic': 'Some magic'}

    @with_magic
    def foo(happened='happened'):
        return magic, happened

    assert(foo() == ('Some magic', 'happened'))

