import pytest
from main import LinkedList

def test_append():
    llist = LinkedList()
    llist.append(1)
    assert str(llist) == "1 "
    llist.append(2)
    assert str(llist) == "1 2 "

def test_sort_list():
    llist = LinkedList()
    llist.append(3)
    llist.append(1)
    llist.append(2)
    llist.sort_list()
    assert str(llist) == "1 2 3 "

def test_empty_list():
    llist = LinkedList()
    llist.sort_list()
    assert str(llist) == ""
