import pytest
import tqv2

@pytest.fixture
def with_taskqueue():
    TQ = tqv2.TaskQueue()
    return TQ

def test_run_accepts_none(with_taskqueue):
    assert with_taskqueue.run(input=None,sequence=['None'])
