"""
Test NonNullType, the red-headed step child of the nulltype
module
"""


from nulltype import NonNullType

Extant = NonNullType("Extant")
Something = NonNullType("Something")
Flubber = NonNullType("Flubber")

nonnulls = [Extant, Something, Flubber]


def test_doc_example():
    Full = NonNullType('Full')

    assert bool(Full) is True
    assert len(Full) == 1
    assert list(Full) == [Full]
    assert Full.some_attribute is Full
    assert Full[22] is Full
    assert Full("hey", 12) is Full


def test_bool():
    for n in nonnulls:
        assert bool(n)


def test_if():
    for n in nonnulls:
        if not n:
            assert False


def test_getitem():
    assert Something[33] is Something
    assert Something["yo"] is Something


def test_setitem():
    Flubber[33] = 1.134
    assert Flubber[33] is Flubber


def test_getattr():
    for nonnull in nonnulls:
        assert nonnull.attribute is nonnull
        assert nonnull.other is nonnull
        assert nonnull.attribute.other.another is nonnull
        assert nonnull.other.attribute.another is nonnull
        assert nonnull.another.attribute.other is nonnull


def test_getattr_getitem():
    assert Something[12].something[33].lazy is Something

    SwedishChef = NonNullType('SwedishChef')
    alt = SwedishChef

    assert alt.swedish.chef.bork.bork.bork is SwedishChef
    # tip of the hat to the Usenet of yore


def test_setattr():
    for nonnull in nonnulls:
        attrs = getattr(nonnull, '__dict__')
        nonnull.one = 44
        nonnull.this.that.the_other = 444
        assert getattr(nonnull, '__dict__') == attrs
        # ie, after attribute changes, assert that none have chagned


def test_iteration():
    for nonnull in nonnulls:
        assert len(nonnull) == 1
        assert list(nonnull) == [nonnull]
        for n in nonnull:
            assert n is nonnull


def test_call():
    for nonnull in nonnulls:
        assert nonnull() is nonnull
        # now gild the lily
        assert nonnull()["something"] is nonnull
        assert nonnull().something is nonnull


def test_repr():
    names = ["Extant", "Something", "Flubber"]
    for nonnull, name in zip(nonnulls, names):
        assert repr(nonnull) == name


def test_set_name():
    Bozo = NonNullType("Bozo")
    assert str(Bozo) == "Bozo"
    Bozo.__name == "Bozo the Clown"
    assert str(Bozo) == "Bozo"

    # No name changes!
