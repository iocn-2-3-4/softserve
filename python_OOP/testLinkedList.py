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
        self.assertEqual(self.list.get()," test1 ")

    def test_put_two(self):
        self.list.put("test1")
        self.list.put("test2")
        self.assertTrue(self.list.get() == " test1 test2 ")

    def test_delete(self):
        self.list.put("test1")
        self.list.put("test2")
        self.list.put("test3")
        #delete tail
        self.list.delete("test3")
        self.assertTrue(self.list.get() == " test1 test2 ")

        #delete  head
        self.list.delete("test1")
        self.assertTrue(self.list.get() ==  " test2 ")

    def test_delete_value_not_in_list(self):
        self.list.put("test")
        self.list.put("test2")
        self.list.put("test3")
        try:
            self.list.delete("test4")
        except ValueError:
            raise ValueError
        with self.assertRaises(ValueError("Wrong element to delete")):
            self.list.delete("test4")

    def test_delete_empty_list(self):
        with self.assertRaises(ValueError('empty list')):
            self.list.delete("test")

    def test_size_of_list(self):
        self.list.put("test")
        self.list.put("test2")
        self.list.put("test3")
        self.assertTrue(self.list.size() == 3)

    def test_index_of_item(self):
        self.list.put("test")
        self.list.put("test2")
        self.list.put("test3")
        self.assertTrue(self.list.indexOf("test2") == 2)

if __name__ == '__main__':
    unittest.main()
