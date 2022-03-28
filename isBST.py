INT_max = 4294967296
INT_min = -4294967296


class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def isBST(root):
	if checkBST(root, INT_min, INT_max):
		print("it's bst")
	else:
		print("not bst")
	

def checkBST(root, min, max):
	if root == None:
		return True

	if root.data > min and root.data < max and checkBST(root.left, min , root.data) and checkBST(root.right, root.data, max):
		return True
	else:
		return False



root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.righ = Node(3)
# root.right.left = Node(7)
# root.right.right = Node(10)

isBST(root)