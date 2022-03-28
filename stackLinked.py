# 	stack using Linked list


class Node:
	def __init__ (self, data):
		self.data = data 
		self.next  = None


class Stacklink:
	def __init__ (self):
		self.top = None


	def push(self, data):
		temp = Node(data)
		temp.next = self.top 
		self.top = temp

	def pop(self):
		temp = self.top 
		self.top = self.top.next 
		del temp

	def get_element(self):
		temp = self.top 
		return temp.data



stack_1 = Stacklink()

stack_1.push(12)
stack_1.push(13)
stack_1.push(14)
stack_1.push(15)

print(stack_1.get_element())
stack_1.pop()
print(stack_1.get_element())



