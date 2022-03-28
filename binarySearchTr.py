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

	def recur_tree(self, root, value):
		if root == None:
			root = self.make_node(value)

		elif value <= root.data:
			root.left = self.recur_tree(root.left , value)

		else:
			root.right = self.recur_tree(root.right, value)

		return root




	def recur_search(self, root, data):
		if root == None:
			return False

		elif root.data == data:
			return True

		elif data <= root.data :
			return self.recur_search(root.left , data)

		else:
			return self.recur_search(root.right , data)
		
		

	def insert(self, data):
		self.root = self.recur_tree(self.root , data)


	def search(self, data):
		if self.recur_search(self.root, data):
			print("found Element")
		else:
			print("element not found")

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


	def max_h(self, l, r):
		if l > r:
			return l
		else:
			return r 

	def hight_rec(self, root):
		if root == None:
			# -1 becouse we are counting the edges and not nodes
			return -1
		return 1 + self.max_h(self.hight_rec(root.left) , self.hight_rec(root.right))

	def hight(self):
		if self.root is None:
			print("tree is empty")
		else:
			print(self.hight_rec(self.root))



		


tree1 = rootNode()

# tree1.insert(15)
# tree1.insert(10)
# tree1.insert(20)
# tree1.insert(5)
# tree1.insert(8)
# tree1.insert(6)
# tree1.insert(9)
# tree1.insert(17)
# tree1.insert(18)

tree1.insert(5)
tree1.insert(4)
tree1.insert(3)
tree1.insert(2)
tree1.insert(1)
tree1.insert(6)
tree1.insert(7)
tree1.insert(8)

tree1.hight()

tree1.search(8)

tree1.min()

tree1.max()

