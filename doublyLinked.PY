class Node:
	def __init__ (self , data):
		self.data = data
		self.next = None
		self.prev = None


class DoublyList:
	def __init__ (self):
		self.head = None

	def push(self, value):
		newnode = Node(value)
		newnode.next = self.head 

		if self.head != None:
			self.head.perv = newnode
		self.head = newnode


	def printlist(self, node):
		while node is not None:
			print(node.data)
			node = node.next




list1 = DoublyList()



# def insertat_head(x):

# 	newnode = Node(x)

# 	if list1.head == None:
# 		list1.head = newnode
# 	else:
# 		list1.head.prev = newnode 
# 		newnode.next = list1.head
# 		list1.head = newnode


# def print_list():
# 	temp = list1.head 

# 	while temp != None:
# 		print(temp.data)
# 		temp = temp.next

# insertat_head(21)
# insertat_head(22)
# insertat_head(23)
# insertat_head(24)
# insertat_head(25)




list1.push(11)
list1.push(12)
list1.push(13)

list1.printlist(list1.head)
# print_list()





