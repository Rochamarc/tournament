from data_manipulation import formulate_data_for_market_value
from data_generator import define_value_by_age, define_value_by_position, define_value_by_overall, apply_reduction

import unittest

# testing applyreduction
class TestReduction(unittest.TestCase):
    def test_value_equal_1(self):
        with self.assertRaises(ValueError):
            apply_reduction(10, 1)

    def test_value_equal_zero(self):
        with self.assertRaises(ValueError):
            apply_reduction(10, 0)

def test_reduction():
    assert apply_reduction(10, 0.1) == 1



# testing partial value for market value by age
def test_value_by_thirdy_tree_plus():
    assert 5_000 <= define_value_by_age(34, 78) <= 10_000

def test_value_by_else():
    assert 10_000 <= define_value_by_age(21, 78) <= 50_000  

def test_value_by_29_32():
    assert 20_000 <= define_value_by_age(31, 78) <= 40_000

def test_value_by_23_28():
    assert 40_000 <= define_value_by_age(25, 78) <= 100_000

# testing partial value for market value by position
def test_value_by_gk():
    assert 5_000 <= define_value_by_position('GK') <= 10_000

def test_value_by_df():
    assert 5_000 <= define_value_by_position('CB') <= 20_000  

def test_value_by_mid():
    assert 5_000 <= define_value_by_position('AM') <= 50_000

def test_value_by_at():
    assert 10_000 <= define_value_by_position('SS') <= 100_000

# testing partial value for market val by overall
def test_value_50_59():
    assert 1_000 <= define_value_by_overall(58) <= 5_000

def test_value_60_69():
    assert 10_000 <= define_value_by_overall(66) <= 20_000  

def test_value_70_79():
    assert 20_000 <= define_value_by_overall(79) <= 30_000

def test_value_80_89():
    assert 50_000 <= define_value_by_overall(87) <= 60_000

def test_value_90_higher():
    assert 70_000 <= define_value_by_overall(98) <= 90_000


class TestDataMarket(unittest.TestCase):
    # define three lists
    a = [
        [ 1,'1997', 'GK' ],
        [ 2,'1996', 'CB' ],
        [ 3,'1995', 'AM' ],
    ]

    b = [
        [78, 1],
        [77, 2],
        [87, 3],
    ]

    c = [
        [ 1,'1997', 'GK', 78 ],
        [ 2,'1996', 'CB', 77 ],
        [ 3,'1995', 'AM', 87 ],
    ]

    # test data for market value
    def test_data_for_market_value(self):
        assert formulate_data_for_market_value(self.a, self.b) == self.c
    
    def test_data_with_diff_length(self):
        b = self.b.copy()
        b.remove(b[-1])

        with self.assertRaises(Exception):
            formulate_data_for_market_value(self.a, b)