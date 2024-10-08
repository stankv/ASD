# Тестирование функции вставки узла newNode после заданного узла afterNode - insert(afterNode, newNode)
import unittest
from DoubleLinkedList import Node, DoubleLinkedList


# РЕГРЕССИОННЫЕ ТЕСТЫ
class insert_test(unittest.TestCase):


    # 1. Если afterNode = None и список пустой, новый элемент первый в списке
    def test_regression1(self):
        d_list = DoubleLinkedList()
        n1 = Node(10)
        d_list.insert(None, n1)
        self.assertEqual(d_list.head, n1)


    # 2. Если afterNode = None и список не пустой (единичный), новый элемент последний в списке
    def test_regression2(self):
        n1 = Node(10)
        d_list = DoubleLinkedList()
        d_list.add_in_tail(n1)
        n2 = Node(20)
        d_list.insert(None, n2)
        self.assertEqual(d_list.tail, n2)


    # 3. Если afterNode = None и список не пустой (не единичный), новый элемент последний в списке
    def test_regression3(self):
        n1 = Node(10)
        n2 = Node(20)
        n3 = Node(30)
        n4 = Node(40)
        n5 = Node(50)
        d_list = DoubleLinkedList()
        d_list.add_in_tail(n1)
        d_list.add_in_tail(n2)
        d_list.add_in_tail(n3)
        d_list.add_in_tail(n4)
        d_list.add_in_tail(n5)
        n0 = Node(1000)
        d_list.insert(None, n0)
        self.assertEqual(d_list.tail, n0)


    # 4. Если afterNode != None и список пустой
    def test_regression4(self):
        d_list = DoubleLinkedList()
        n1 = Node(10)
        n2 = Node(20)
        d_list.insert(n1, n2)
        self.assertEqual(d_list.head, None)


    # 5. Если afterNode в списке и равен первому узлу
    def test_regression5(self):
        n1 = Node(10)
        n2 = Node(20)
        n3 = Node(30)
        n4 = Node(40)
        n5 = Node(50)
        d_list = DoubleLinkedList()
        d_list.add_in_tail(n1)
        d_list.add_in_tail(n2)
        d_list.add_in_tail(n3)
        d_list.add_in_tail(n4)
        d_list.add_in_tail(n5)
        n0 = Node(1000)
        d_list.insert(n1, n0)
        self.assertEqual(all_nodes(d_list), [n1,n0,n2,n3,n4,n5])


    # 6. Если afterNode в списке в середине
    def test_regression6(self):
        n1 = Node(10)
        n2 = Node(20)
        n3 = Node(30)
        n4 = Node(40)
        n5 = Node(50)
        d_list = DoubleLinkedList()
        d_list.add_in_tail(n1)
        d_list.add_in_tail(n2)
        d_list.add_in_tail(n3)
        d_list.add_in_tail(n4)
        d_list.add_in_tail(n5)
        n0 = Node(1000)
        d_list.insert(n3, n0)
        self.assertEqual(all_nodes(d_list), [n1,n2,n3,n0,n4,n5])


    # 7. Если afterNode в списке = предпоследнему узлу
    def test_regression7(self):
        n1 = Node(10)
        n2 = Node(20)
        n3 = Node(30)
        n4 = Node(40)
        n5 = Node(50)
        d_list = DoubleLinkedList()
        d_list.add_in_tail(n1)
        d_list.add_in_tail(n2)
        d_list.add_in_tail(n3)
        d_list.add_in_tail(n4)
        d_list.add_in_tail(n5)
        n0 = Node(1000)
        d_list.insert(n4, n0)
        self.assertEqual(all_nodes(d_list), [n1,n2,n3,n4,n0,n5])


    # 8. Если afterNode в списке = последнему узлу
    def test_regression8(self):
        n1 = Node(10)
        n2 = Node(20)
        n3 = Node(30)
        n4 = Node(40)
        n5 = Node(50)
        d_list = DoubleLinkedList()
        d_list.add_in_tail(n1)
        d_list.add_in_tail(n2)
        d_list.add_in_tail(n3)
        d_list.add_in_tail(n4)
        d_list.add_in_tail(n5)
        n0 = Node(1000)
        d_list.insert(n5, n0)
        self.assertEqual(all_nodes(d_list), [n1,n2,n3,n4,n5,n0])


# Ф-я создания массива узлов всего списка
def all_nodes(self):
    S = []
    node = self.head
    while node is not None:
        S.append(node)
        node = node.next
    return S


if __name__ == '__main__':
    unittest.main()
