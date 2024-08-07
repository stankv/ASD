# Тестирование функции поиска всех узлов связанного списка find_all(val) по конкретному значению 
# (функция возвращает стандартный питоновский список найденных узлов)
import unittest
from DoubleLinkedList import Node, DoubleLinkedList
import random


# РЕГРЕССИОННЫЕ ТЕСТЫ
class find_all_test(unittest.TestCase):


    # 1. Пустой связанный список
    def test_regression1(self):
        d_list = DoubleLinkedList()
        self.assertEqual(d_list.find_all(10), [])


    # 2. Связанный список только с одним узлом - узел с таким значением есть в списке
    def test_regression2(self):
        n1 = Node(10)
        d_list = DoubleLinkedList()
        d_list.add_in_tail(n1)
        S = d_list.find_all(10)
        print(S)
        self.assertEqual(S[0], n1)


    # 3. Связанный список только с одним узлом - узла с таким значением нет в списке
    def test_regression3(self):
        n1 = Node(10)
        d_list = DoubleLinkedList()
        d_list.add_in_tail(n1)
        S = d_list.find_all(20)
        self.assertNotEqual(S, n1)


    # 4. Связанный список из 10 узлов с одинаковыми значениями - узлы с таким значением есть в списке
    def test_regression4(self):
        n1 = Node(10)
        n2 = Node(10)
        n3 = Node(10)
        n4 = Node(10)
        n5 = Node(10)
        n6 = Node(10)
        n7 = Node(10)
        n8 = Node(10)
        n9 = Node(10)
        n10 = Node(10)
        d_list = DoubleLinkedList()
        d_list.add_in_tail(n1)
        d_list.add_in_tail(n2)
        d_list.add_in_tail(n3)
        d_list.add_in_tail(n4)
        d_list.add_in_tail(n5)
        d_list.add_in_tail(n6)
        d_list.add_in_tail(n7)
        d_list.add_in_tail(n8)
        d_list.add_in_tail(n9)
        d_list.add_in_tail(n10)
        S = d_list.find_all(10)
        self.assertEqual(S, [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10])


    # 5. Связанный список из 10 узлов с одинаковыми значениями - узла с таким значением нет в списке
    def test_regression5(self):
        n1 = Node(10)
        n2 = Node(10)
        n3 = Node(10)
        n4 = Node(10)
        n5 = Node(10)
        n6 = Node(10)
        n7 = Node(10)
        n8 = Node(10)
        n9 = Node(10)
        n10 = Node(10)
        d_list = DoubleLinkedList()
        d_list.add_in_tail(n1)
        d_list.add_in_tail(n2)
        d_list.add_in_tail(n3)
        d_list.add_in_tail(n4)
        d_list.add_in_tail(n5)
        d_list.add_in_tail(n6)
        d_list.add_in_tail(n7)
        d_list.add_in_tail(n8)
        d_list.add_in_tail(n9)
        d_list.add_in_tail(n10)
        S = d_list.find_all(20)
        self.assertNotEqual(S, [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10])


    # 6. Связанный список из 10 узлов с разными значениями - узел с таким значением есть в списке
    def test_regression6(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n5 = Node(5)
        n6 = Node(6)
        n7 = Node(7)
        n8 = Node(8)
        n9 = Node(9)
        n10 = Node(10)
        d_list = DoubleLinkedList()
        d_list.add_in_tail(n1)
        d_list.add_in_tail(n2)
        d_list.add_in_tail(n3)
        d_list.add_in_tail(n4)
        d_list.add_in_tail(n5)
        d_list.add_in_tail(n6)
        d_list.add_in_tail(n7)
        d_list.add_in_tail(n8)
        d_list.add_in_tail(n9)
        d_list.add_in_tail(n10)
        k = random.randint(1, 10)
        S = d_list.find_all(k)
        if k == 1:
            node = n1
        elif k == 2:
            node = n2
        elif k == 3:
            node = n3
        elif k == 4:
            node = n4
        elif k == 5:
            node = n5
        elif k == 6:
            node = n6
        elif k == 7:
            node = n7
        elif k == 8:
            node = n8
        elif k == 9:
            node = n9
        elif k == 10:
            node = n10
        self.assertEqual(S[0], node)


    # 7. Связанный список из 10 узлов с разными значениями - узлы с таким значением есть в списке
    def test_regression7(self):
        n1 = Node(10)
        n2 = Node(10)
        n3 = Node(3)
        n4 = Node(10)
        n5 = Node(10)
        n6 = Node(6)
        n7 = Node(10)
        n8 = Node(8)
        n9 = Node(10)
        n10 = Node(10)
        d_list = DoubleLinkedList()
        d_list.add_in_tail(n1)
        d_list.add_in_tail(n2)
        d_list.add_in_tail(n3)
        d_list.add_in_tail(n4)
        d_list.add_in_tail(n5)
        d_list.add_in_tail(n6)
        d_list.add_in_tail(n7)
        d_list.add_in_tail(n8)
        d_list.add_in_tail(n9)
        d_list.add_in_tail(n10)
        S = d_list.find_all(10)
        self.assertEqual(S, [n1,n2,n4,n5,n7,n9,n10])


if __name__ == '__main__':
    unittest.main()