import unittest

from linkedList import linkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = linkedList()

    def tearDown(self):
        self.list = None

    def test_put(self):
        self.list.put("test1")
        self.assertTrue(self.list.head.get_data() == "test1")
        self.assertTrue(self.list.head.get_next() is None)

    def test_put_two(self):
        self.list.put("test1")
        self.list.put("test2")
        self.assertTrue(self.list.head.get_data() == "test2")
        head_next = self.list.head.get_next()
        self.assertTrue(head_next.get_data() == "test1")

    def test_nextNode(self):
        self.list.put("test")
        self.list.put("test2")
        self.list.put("test3")

        self.assertTrue(self.list.head.get_data() == "test3")

        head_next = self.list.head.get_next()
        self.assertTrue(head_next.get_data() == "test2")

        last = head_next.get_next()
        self.assertTrue(last.get_data() == "test")

    def test_positive_get(self):
        self.list.put("test")
        self.list.put("test2")
        self.list.put("test3")

        found = self.list.get("test")
        self.assertTrue(found.get_data() == "test")

        found = self.list.get("test2")
        self.assertTrue(found.get_data() == "test2")

        found = self.list.get("test")
        self.assertTrue(found.get_data() == "test")

    def test_getNone(self):
        self.list.put("test")
        self.list.put("test2")

        # make sure reg get works
        found = self.list.get("test")

        self.assertTrue(found.get_data() == "test")

        with self.assertRaises(ValueError):
            self.list.get("test")

    def test_delete(self):
        self.list.put("test")
        self.list.put("test2")
        self.list.put("test3")

        # Delete the list head
        self.list.delete("test3")
        self.assertTrue(self.list.head.get_data() == "test2")

        # Delete the list tail
        self.list.delete("test")
        self.assertTrue(self.list.head.get_next() is None)

    def test_delete_value_not_in_list(self):
        self.list.put("test")
        self.list.put("test2")
        self.list.put("test3")

        with self.assertRaises(ValueError):
            self.list.delete("WRONG")

    def test_delete_empty_list(self):
        with self.assertRaises(ValueError):
            self.list.delete("WRONG")

    def test_delete_next_reassignment(self):
        self.list.put("test")
        self.list.put("testing")
        self.list.put("test2")
        self.list.put("test3")

        self.list.delete("test2")
        self.list.delete("Cid")
