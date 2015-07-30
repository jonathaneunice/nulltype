
from nulltype import NullType, Nothing, Null

Prohibited = NullType("Prohibited")
Transient  = NullType("Transient")

nulls = [Prohibited, Transient, Nothing, Null]

def test_doc_example():
    Empty = NullType('Empty')

    assert bool(Empty) == False
    assert len(Empty) == 0
    assert list(Empty) == []
    assert Empty.some_attribute is Empty
    assert Empty[22] is Empty
    assert Empty("hey", 12) is Empty

def test_bool():
    for n in nulls:
        assert not bool(n)

def test_if():
    for n in nulls:
        if n:
            assert False

def test_getitem():
    assert Nothing[33] is Nothing
    assert Nothing["yo"] is Nothing

def test_setitem():
    pass

def test_getattr():
    for null in nulls:
        assert null.attribute is null
        assert null.other is null
        assert null.attribute.other.another is null
        assert null.other.attribute.another is null
        assert null.another.attribute.other is null

def test_getattr_getitem():
    assert Nothing[12].something[33].lazy is Nothing

    SwedishChef = NullType('SwedishChef')
    alt = SwedishChef

    assert alt.swedish.chef.bork.bork.bork is SwedishChef
    # tip of the hat to the Usenet of yore

def test_setattr():
    for null in nulls:
        attrs = getattr(null, '__dict__')
        null.one = 44
        null.this.that.the_other = 444
        assert getattr(null, '__dict__') == attrs

def test_iteration():
    for null in nulls:
        assert len(null) == 0
        assert list(null) == []
        for n in null:
            assert False

def test_call():
    for null in nulls:
        assert null() is null
        # now gild the lily
        assert null()["something"] is null
        assert null().something is null

def test_repr():
    names = ["Prohibited", "Transient", "Nothing"]
    for null, name in zip(nulls, names):
        assert repr(null) == name
