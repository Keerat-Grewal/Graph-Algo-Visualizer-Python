import unittest
from visual import *

#THIS IS THE TEST CASE FILE

class TestList(unittest.TestCase):

    def test_remove_dup_connections_one(self):
        connections = [1, 2, 3, 4, 5]
        remove_dup_connections(connections)
        self.assertEqual(connections, [1, 2, 3, 4, 5])

    def test_remove_dup_connections_two(self):
        connections2 = [1, 2, 2, 1]
        remove_dup_connections(connections2)
        self.assertEqual(connections2, [1, 2])

    def test_remove_dup_connections_three(self):
        connections = [1, 2, 2, 1, 1]
        remove_dup_connections(connections)
        self.assertEqual(connections, [1, 2, 1])

    def test_remove_dup_connections_four(self):
        connections = [1, 2, 2]
        remove_dup_connections(connections)
        self.assertEqual(connections, [1, 2, 2])

    def test_remove_dup_connections_five(self):
        connections = [1, 2, 2, 3, 4, 5, 2, 1, 5, 9, 3, 2]
        remove_dup_connections(connections)
        self.assertEqual(connections, [1, 2, 2, 3, 4, 5, 5, 9])

if __name__ == '__main__':
    unittest.main()
