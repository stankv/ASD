# Тестирование функции поиска узла по заданному значению find(self, val) 
# по заданному значению - delete(val, all)
import unittest
from DoubleLinkedList import Node, DoubleLinkedList
import random

# РЕГРЕССИОННЫЕ ТЕСТЫ
class find_test(unittest.TestCase):


    # 1. Пустой связанный список, поиск "произвольного" узла
    def test_regression1(self):
        k = random.randint(1,1000)
        n1 = Node(k)
        d_list = DoubleLinkedList()
        self.assertEqual(d_list.find(k), None)


    # 2. Непустой список, поиск узла, которого нет в списке
    def test_regression2(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        d_list = DoubleLinkedList()
        d_list.add_in_tail(n1)
        d_list.add_in_tail(n2)
        d_list.add_in_tail(n3)
        k = random.randint(100,1000)
        self.assertEqual(d_list.find(k), None)


    # 3. Непустой список, поиск узла со значением None
    def test_regression3(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        d_list = DoubleLinkedList()
        d_list.add_in_tail(n1)
        d_list.add_in_tail(n2)
        d_list.add_in_tail(n3)
        k = None
        self.assertEqual(d_list.find(k), None)


    # 4. Непустой список, поиск существующего узла по значению: узел в начале
    def test_regression4(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n5 = Node(5)
        d_list = DoubleLinkedList()
        d_list.add_in_tail(n1)
        d_list.add_in_tail(n2)
        d_list.add_in_tail(n3)
        d_list.add_in_tail(n4)
        d_list.add_in_tail(n5)
        self.assertEqual(d_list.find(1), n1)


    # 5. Непустой список, поиск существующего узла по значению: узел в конце
    def test_regression5(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n5 = Node(5)
        d_list = DoubleLinkedList()
        d_list.add_in_tail(n1)
        d_list.add_in_tail(n2)
        d_list.add_in_tail(n3)
        d_list.add_in_tail(n4)
        d_list.add_in_tail(n5)
        self.assertEqual(d_list.find(5), n5)


    # 6. Непустой список, поиск существующего узла по значению: узел в середине
    def test_regression6(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n5 = Node(5)
        d_list = DoubleLinkedList()
        d_list.add_in_tail(n1)
        d_list.add_in_tail(n2)
        d_list.add_in_tail(n3)
        d_list.add_in_tail(n4)
        d_list.add_in_tail(n5)
        self.assertEqual(d_list.find(3), n3)


    # 7. Непустой список, поиск первого существующего узла по значению
    def test_regression7(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(2)
        n5 = Node(5)
        d_list = DoubleLinkedList()
        d_list.add_in_tail(n1)
        d_list.add_in_tail(n2)
        d_list.add_in_tail(n3)
        d_list.add_in_tail(n4)
        d_list.add_in_tail(n5)
        self.assertEqual(d_list.find(2), n2)


if __name__ == '__main__':
    unittest.main()