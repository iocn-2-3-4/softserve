import unittest
# import linkedList
from linkedList import linkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = linkedList()

    def tearDown(self):
        self.list = None

    def test_put(self):
        self.list.put("test1")
        self.assertEqual(self.list.get(),"test1")

    def test_put_two(self):
        self.list.put("test1")
        self.list.put("test2")
        self.assertTrue(self.list.get() == "test test2")

    def test_delete(self):
        self.list.put("test")
        self.list.put("test2")
        self.list.put("test3")

        # Delete the list head
        self.list.delete("test3")
        self.assertTrue(self.list.get == "test2")

        # Delete the list tail
        self.list.delete("test")
        self.assertTrue(self.list.get is None)

    def test_delete_value_not_in_list(self):
        self.list.put("test")
        self.list.put("test2")
        self.list.put("test3")

        with self.assertRaises(ValueError):
            self.list.delete("WRONG")

    def test_delete_empty_list(self):
        with self.assertRaises(ValueError):
            self.list.delete("WRONG")


if __name__ == '__main__':
    unittest.main()

# self.list.put("test1")
# self.list.get()

