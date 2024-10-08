# ДЕРЕВЬЯ.
# Построение сбалансированного бинарного дерева поиска из данных неотсортированного массива.

class BSTNode:
	
    def __init__(self, key, parent):
        self.NodeKey = key # ключ узла
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок
        self.Level = 0 # уровень узла
        
class BalancedBST:
		
    def __init__(self):
    	self.Root = None # корень дерева


    # создаём дерево с нуля из неотсортированного массива a
    def GenerateTree(self, a):
	
        def AddNodeToTree(parent, a, level=0):    # возвращает коренной узел!
            if a == []:
                return
            index_center = len(a) // 2
            Node = BSTNode(a[index_center], parent)
            Node.Level = level
            Node.Parent = parent
            level += 1
            Node.LeftChild = AddNodeToTree(Node, a[:index_center], level)
            Node.RightChild = AddNodeToTree(Node, a[index_center + 1:], level)
            print(Node.NodeKey)
            return Node

        if len(a) == 1:
            self.Root = BSTNode(a[0], None)
            return self.Root
        elif a == [] or a is None:
            return None
        elif len(a) > 1:
            a.sort()
            self.Root = AddNodeToTree(None, a)
            return self.Root


    # проверка является ли дерево сбалансированным
    def IsBalanced(self, root_node):

        def DepthSubtree(root_node):
            current_depth = 0
            if root_node.LeftChild:
                current_depth = max(current_depth,  DepthSubtree(root_node.LeftChild))
            if root_node.RightChild:
                current_depth = max(current_depth,  DepthSubtree(root_node.RightChild))
            return current_depth + 1
        
        depth_of_left_subtree = 0
        depth_of_right_subtree = 0
        if root_node.LeftChild:
            self.IsBalanced(root_node.LeftChild)
            depth_of_left_subtree = DepthSubtree(root_node.LeftChild)
        if root_node.RightChild:
            self.IsBalanced(root_node.RightChild)
            depth_of_right_subtree = DepthSubtree(root_node.RightChild)
        
        if abs(depth_of_left_subtree - depth_of_right_subtree) <=1:
            return True
        else:
            return False


"""z = [7,2,3,1,4,8,9,6,10,5,0]
My_Tree = BalancedBST()
node = My_Tree.GenerateTree(z)
print()
print("node:", node.NodeKey, "parent:", node.Parent, 'level:', node.Level)
print("left:", node.LeftChild.NodeKey, "right:", node.RightChild.NodeKey)
print(node.LeftChild.Parent.NodeKey, node.RightChild.Parent.NodeKey)
print()
node = node.LeftChild
print("node:", node.NodeKey, "parent:", node.Parent.NodeKey, 'level:', node.Level)
print("left:", node.LeftChild.NodeKey, "right:", node.RightChild.NodeKey)
print(node.LeftChild.Parent.NodeKey, node.RightChild.Parent.NodeKey)
print()
node = node.Parent.RightChild
print("node:", node.NodeKey, "parent:", node.Parent.NodeKey, 'level:', node.Level)
print("left:", node.LeftChild.NodeKey, "right:", node.RightChild.NodeKey)
print(node.LeftChild.Parent.NodeKey, node.RightChild.Parent.NodeKey)
print(My_Tree.IsBalanced(My_Tree.Root))"""