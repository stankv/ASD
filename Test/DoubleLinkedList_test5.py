# Тестирование функции вычисления текущей длины одннаправленного связанного списка len()
import unittest
from DoubleLinkedList import Node, DoubleLinkedList
import random


# РЕГРЕССИОННЫЕ ТЕСТЫ
class len_test(unittest.TestCase):


    # 1. Пустой связанный список
    def test_regression1(self):
        d_list = DoubleLinkedList()
        self.assertEqual(d_list.len(), 0)


    # 2. Связанный список с 1 элементом
    def test_regression2(self):
        n1 = Node(10)
        d_list = DoubleLinkedList()
        d_list.add_in_tail(n1)
        self.assertEqual(d_list.len(), 1)


    # 3. Связанный список случайной длины со случайными значениями узлов
    def test_regression3(self):
        d_list = DoubleLinkedList()
        k = random.randint(1, 1000)
        for i in range(k):
            d_list.add_in_tail(Node(random.randint(1, 1000)))
        self.assertEqual(d_list.len(), k)


if __name__ == '__main__':
    unittest.main()
