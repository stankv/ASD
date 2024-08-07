# Тестирование функции очистки всего содержимого двусвязанного списка clean()
import unittest
from DoubleLinkedList import Node, DoubleLinkedList
import random


# РЕГРЕССИОННЫЕ ТЕСТЫ
class clean_test(unittest.TestCase):


    # 1. Пустой связанный список
    def test_regression1(self):
        d_list = DoubleLinkedList()
        self.assertEqual(d_list.clean(), None)


    # 2. Связанный список с одним узлом
    def test_regression2(self):
        n1 = Node(10)
        d_list = DoubleLinkedList()
        d_list.add_in_tail(n1)
        self.assertEqual(d_list.clean(), None)


    # 3. Связанный список со случайным количеством узлов
    def test_regression3(self):
        d_list = DoubleLinkedList()
        for i in range(random.randint(1, 1000)):
            d_list.add_in_tail(Node(i))
        self.assertEqual(d_list.clean(), None)


if __name__ == '__main__':
    unittest.main()
