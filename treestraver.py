class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class rootNode:
    def __init__(self):
        self.root = None


    def make_node(self, value):
        newNode = Node(value)
        newNode.left = newNode.right = None
        return newNode


    def insert(self, value):
        top = self.root
        temp = None
        
        while top !=None:
            temp = top
            if value <= top.data:
                top = top.left
            else:
                top = top.right
                
        if self.root == None:
            self.root = self.make_node(value)
            
        elif value <= temp.data:
            temp.left = self.make_node(value)
        else:
            temp.right = self.make_node(value)
            

    def min(self):
        if self.root is None:
            print("tree is empty")
        else:
            temp = self.root 
            while temp.left != None:
                temp = temp.left
            print("minimum value", temp.data)

    def max(self):
        if self.root is None:
            print("tree is empty")
        else:
            temp = self.root 
            while temp.right != None:
                temp = temp.right
            print("maximum value", temp.data)


tree1 = rootNode()

tree1.insert(8)
tree1.insert(6)
tree1.insert(2)
tree1.insert(10)
tree1.insert(9)


tree1.min()

tree1.max()