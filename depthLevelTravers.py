class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def pre_order(root):
	if root == None:
		return
	print(root.data)
	pre_order(root.left)
	pre_order(root.right)

def in_order(root):
	if root == None:
		return
	in_order(root.left)
	print(root.data)
	in_order(root.right)

def post_order(root):
	if root == None:
		return
	post_order(root.left)
	post_order(root.right)
	print(root.data)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("pre order")
pre_order(root)

print("inn order")
in_order(root)

print("post order")
post_order(root)