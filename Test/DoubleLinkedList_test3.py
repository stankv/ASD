# Тестирование функции удаления одного узла (all=False)/всех узлов (all=True) 
# по заданному значению - delete(val, all) для двусвязного списка
import unittest
from DoubleLinkedList import Node, DoubleLinkedList


# РЕГРЕССИОННЫЕ ТЕСТЫ
class delete_test(unittest.TestCase):


    # 1. Пустой связанный список, all=False
    def test_regression1(self):
        d_list = DoubleLinkedList()
        n1 = Node(10)
        d_list.delete(10)
        L = node_list(d_list)
        self.assertEqual(L, [])


    # 2. Пустой связанный список, all=True
    def test_regression2(self):
        d_list = DoubleLinkedList()
        n1 = Node(10)
        d_list.delete(10, True)
        L = node_list(d_list)
        self.assertEqual(L, [])


    # 3. Cвязанный список c 1 элементом, all=False
    def test_regression3(self):
        d_list = DoubleLinkedList()
        n1 = Node(10)
        d_list.add_in_tail(n1)
        d_list.delete(10)
        L = node_list(d_list)
        self.assertEqual(L, [])


    # 4. Cвязанный список c 1 элементом, all=True
    def test_regression4(self):
        d_list = DoubleLinkedList()
        n1 = Node(10)
        d_list.add_in_tail(n1)
        d_list.delete(10, True)
        L = node_list(d_list)
        self.assertEqual(L, [])


    # 5. Cвязанный список, удаление первого элемента, all=False
    def test_regression5(self):
        d_list = DoubleLinkedList()
        n1 = Node(10)
        n2 = Node(20)
        n3 = Node(30)
        d_list.add_in_tail(n1)
        d_list.add_in_tail(n2)
        d_list.add_in_tail(n3)
        d_list.delete(10)
        L = node_list(d_list)
        self.assertEqual(L, [n2,n3])


    # 6. Cвязанный список, удаление последнего элемента, all=False
    def test_regression6(self):
        d_list = DoubleLinkedList()
        n1 = Node(10)
        n2 = Node(20)
        n3 = Node(30)
        d_list.add_in_tail(n1)
        d_list.add_in_tail(n2)
        d_list.add_in_tail(n3)
        d_list.delete(30)
        L = node_list(d_list)
        self.assertEqual(L, [n1,n2])


    # 7. Cвязанный список, удаление предпоследнего элемента, all=False
    def test_regression7(self):
        d_list = DoubleLinkedList()
        n1 = Node(10)
        n2 = Node(20)
        n3 = Node(30)
        n4 = Node(40)
        d_list.add_in_tail(n1)
        d_list.add_in_tail(n2)
        d_list.add_in_tail(n3)
        d_list.add_in_tail(n4)
        d_list.delete(30)
        L = node_list(d_list)
        self.assertEqual(L, [n1,n2,n4])


    # 8. Cвязанный список, удаление всех одинаковых элементов, all=True
    def test_regression8(self):
        d_list = DoubleLinkedList()
        n1 = Node(10)
        n2 = Node(10)
        n3 = Node(30)
        n4 = Node(40)
        n5 = Node(10)
        n6 = Node(40)
        n7 = Node(10)
        n8 = Node(40)
        n9 = Node(10)
        n10 = Node(10)
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
        d_list.delete(10, True)
        L = node_list(d_list)
        self.assertEqual(L, [n3,n4,n6,n8])


    # 9. Cвязанный список, удаление всех одинаковых элементов подряд в середине, all=True
    def test_regression9(self):
        d_list = DoubleLinkedList()
        n1 = Node(10)
        n2 = Node(20)
        n3 = Node(30)
        n4 = Node(40)
        n5 = Node(40)
        n6 = Node(40)
        n7 = Node(40)
        n8 = Node(40)
        n9 = Node(90)
        n10 = Node(100)
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
        d_list.delete(40, True)
        L = node_list(d_list)
        self.assertEqual(L, [n1,n2,n3,n9,n10])


# Ф-я формирования массива узлов после применения удаления
def node_list(d_list):
    S = []
    node = d_list.head
    while node is not None:
        S.append(node)
        node = node.next
    return S


if __name__ == '__main__':
    unittest.main()