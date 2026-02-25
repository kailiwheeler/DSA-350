from q import *

def test_is_empty():
    q = Queue()
    assert q.is_empty() # is true
def test_add():
    q = Queue()
    q.add('Ann')
    assert q.head.data == 'Ann'
    q.add('Beth')
    assert q.head.data == 'Ann'
    next_node = q.head.next
    assert q.head.next.data == 'Beth'
def test_size():
    q = Queue()
    assert q.size == 0
    q.add('Ann')
    assert q.size == 1
    q.add('Beth')
    q.add('Carry')
    q.add('David')
    assert q.size == 4
def test_left():
    q = Queue()
    q.add('Ann')
    q.add('Beth')
    q.add('Carry')
    q.add('David')
    assert q.head.data == 'Ann'
    n = q.pop_left()
    assert q.head.data == 'Beth'
    assert n.data == 'Ann'

    


