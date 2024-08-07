# Тестирование функции очистки всего содержимого связанного списка clean()
import unittest
from SimpleLinkedList import Node, LinkedList
import random


# РЕГРЕССИОННЫЕ ТЕСТЫ
class clean_test(unittest.TestCase):


    # 1. Пустой связанный список
    def test_regression1(self):
        s_list = LinkedList()
        self.assertEqual(s_list.clean(), None)


    # 2. Связанный список с одним узлом
    def test_regression2(self):
        n1 = Node(10)
        s_list = LinkedList()
        s_list.add_in_tail(n1)
        self.assertEqual(s_list.clean(), None)


    # 3. Связанный список со случайным количеством узлов
    def test_regression3(self):
        s_list = LinkedList()
        for i in range(random.randint(1, 1000)):
            s_list.add_in_tail(Node(i))
        self.assertEqual(s_list.clean(), None)


if __name__ == '__main__':
    unittest.main()