"""Tests for Lab 4 methods.
Course: CPE202
Quarter: Spring 2020
Author: Henry Berman
"""


import unittest
from queue_linked import *
from queue_array import *

class TestCases(unittest.TestCase):
    def test_queue_linked1(self):
        queue = QueueLinked()
        self.assertEqual(2, queue.capacity)
        self.assertEqual(0, queue.size())
        self.assertTrue(queue.is_empty())
        self.assertEqual(None, queue.front)
        self.assertEqual(None, queue.rear)
        queue2 = QueueLinked()
        self.assertEqual(queue, queue2)
        self.assertEqual('None', str(queue))

    def test_queue_linked2(self):
        queue = QueueLinked()
        queue.enqueue(1)
        self.assertEqual(1, queue.front.val)
        self.assertEqual(1, queue.rear.val)
        self.assertEqual(1, queue.num_items)
        queue.enqueue(2)
        self.assertRaises(IndexError, queue.enqueue, 3)

    def test_queue_linked3(self):
        queue = QueueLinked(4)
        lst = []
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        self.assertTrue(queue.is_full)
        for i in range(4):
            lst.append(queue.dequeue())
        self.assertEqual([1, 2, 3, 4], lst)
        self.assertRaises(IndexError, queue.dequeue)

    def test_queue_array1(self):
        queue = QueueArray()
        self.assertEqual(2, queue.capacity)
        self.assertEqual(0, queue.size())
        self.assertTrue(queue.is_empty())
        queue2 = QueueArray()
        self.assertEqual(queue, queue2)
        self.assertEqual('[None, None, None]', str(queue))

    def test_queue_array2(self):
        queue = QueueArray()
        queue.enqueue(1)
        self.assertEqual(1, queue.num_items)
        queue.enqueue(2)
        self.assertRaises(IndexError, queue.enqueue, 3)

    def test_queue_array3(self):
        queue = QueueArray(4)
        lst = []
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        self.assertTrue(queue.is_full)
        for i in range(4):
            lst.append(queue.dequeue())
        self.assertEqual([1, 2, 3, 4], lst)
        self.assertRaises(IndexError, queue.dequeue)


if __name__ == '__main__':
    unittest.main()
