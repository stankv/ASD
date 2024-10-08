# Тестирование функции вычисления текущей длины одннаправленного связанного списка len()
import unittest
from SimpleLinkedList import Node, LinkedList
import random


# РЕГРЕССИОННЫЕ ТЕСТЫ
class len_test(unittest.TestCase):


    # 1. Пустой связанный список
    def test_regression1(self):
        s_list = LinkedList()
        self.assertEqual(s_list.len(), 0)


    # 2. Связанный список с 1 элементом
    def test_regression2(self):
        n1 = Node(10)
        s_list = LinkedList()
        s_list.add_in_tail(n1)
        self.assertEqual(s_list.len(), 1)


    # 3. Связанный список случайной длины со случайными значениями узлов
    def test_regression3(self):
        s_list = LinkedList()
        k = random.randint(1, 1000)
        for i in range(k):
            s_list.add_in_tail(Node(random.randint(1, 1000)))
        self.assertEqual(s_list.len(), k)


if __name__ == '__main__':
    unittest.main()
