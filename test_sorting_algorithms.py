import unittest
from sorting_algorithms import quickSort, countingSort, mergeSort

def makeTest(function):

    class Test_Sort(unittest.TestCase):

        def test_basic(self):
            arr = [3, 2, 1]
            self.assertEqual(function(arr), [1, 2, 3])

        def test_empty(self):
            arr = []
            self.assertEqual(function(arr), [])

        def test_negative(self):
            arr = [10, -1, -2, 3]
            self.assertEqual(function(arr), [-2, -1, 3, 10])

    return Test_Sort

class TestQuickSortImplementation(makeTest(quickSort)):
    pass

class TestCountingSortImplementation(makeTest(countingSort)):
    pass

class TestMergeSortImplementation(makeTest(mergeSort)):
    pass