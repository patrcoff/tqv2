import pytest

def test_basic_import():
    import tqv2
    assert tqv2.taskqueue._placeholder() == None