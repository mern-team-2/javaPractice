class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def minValue(temp):
	while temp.left != None:
		temp = temp.left
	return temp


def deleteNode(root, value):
	if root == None:
		return root

	elif root.data > value:
		root.left = deleteNode(root.left, value)
	elif root.data < value:
		root.right = deleteNode(root.right, value)
	else:
		# if its a leaf node
		if root.left == None and root.right == None:
			del root 
			root = None
		# if it has only one child
		elif root.left == None:
			temp = root.right
			root = root.right
			del temp
		elif root.right == None:
			temp = root.left
			root = root.left
			del temp
		else:
			temp = minValue(root.right)
			root.data = temp.data 
			root.right = deleteNode(root.right, temp.data)
		
		return root

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.righ = Node(3)
root.right.left = Node(7)
root.right.right = Node(8)


deleteNode(root, 5)
print(root.right.data)