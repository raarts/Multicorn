from nose.tools import assert_equal, assert_not_equal

from kalamar.request import Condition, Not, And, Or

def test_hash_condition():
    c1 = Condition("name","<","tortue")
    c2 = Condition("name", "<", "tortue")
    c3 = Condition("name", "<", "hibou")
    c4 = Condition("name", ">", "tortue")
    c5 = Condition("bob", "<", "tortue")

    assert_equal(hash(c1), hash(c2))
    assert_not_equal(hash(c1), hash(c3))
    assert_not_equal(hash(c1), hash(c4))
    assert_not_equal(hash(c1), hash(c5))


def test_hash_and():
    c1 = Condition("name","<","tortue")
    c2 = Condition("name", "<", "hibou")
    c3 = Condition("name", "<", "tortue")
    
    c4 = And(c1, c2)
    c5 = And(c3, c2)
    c6 = And(c1, c3)

    assert_equal(hash(c4), hash(c5))
    assert_not_equal(hash(c4), hash(c6))

def test_hash_or():
    c1 = Condition("name","<","tortue")
    c2 = Condition("name", "<", "hibou")
    c3 = Condition("name", "<", "tortue")
    
    c4 = Or(c1, c2)
    c5 = Or(c3, c2)
    c6 = Or(c1, c3)

    assert_equal(hash(c4), hash(c5))
    assert_not_equal(hash(c4), hash(c6))

def test_hash_not():
    c1 = Condition("name","<","tortue")
    c2 = Condition("name", "<", "hibou")
    c3 = Condition("name", "<", "tortue")
    
    c4 = Not(c1)
    c5 = Not(c3)
    c6 = Not(c2)

    assert_equal(hash(c4), hash(c5))
    assert_not_equal(hash(c4), hash(c6))

def test_eq_condition():
    c1 = Condition("name","<","tortue")
    c2 = Condition("name", "<", "tortue")
    c3 = Condition("name", "<", "hibou")
    c4 = Condition("name", ">", "tortue")
    c5 = Condition("bob", "<", "tortue")

    assert_equal(c1, c2)
    assert_not_equal(c1, c3)
    assert_not_equal(c1, c4)
    assert_not_equal(c1, c5)


def test_and():
    c1 = Condition("name","<","tortue")
    c2 = Condition("name", "<", "hibou")
    c3 = Condition("name", "<", "tortue")
    
    c4 = And(c1, c2)
    c5 = And(c3, c2)
    c6 = And(c1, c3)

    assert_equal(c4, c5)
    assert_not_equal(c4, c6)

def test_or():
    c1 = Condition("name","<","tortue")
    c2 = Condition("name", "<", "hibou")
    c3 = Condition("name", "<", "tortue")
    
    c4 = Or(c1, c2)
    c5 = Or(c3, c2)
    c6 = Or(c1, c3)

    assert_equal(c4, c5)
    assert_not_equal(c4, c6)

def test_not():
    c1 = Condition("name","<","tortue")
    c2 = Condition("name", "<", "hibou")
    c3 = Condition("name", "<", "tortue")
    
    c4 = Not(c1)
    c5 = Not(c3)
    c6 = Not(c2)

    assert_equal(c4, c5)
    assert_not_equal(c4, c6)