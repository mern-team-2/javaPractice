## queue using link list 

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Linked:
	def __init__(self):
		self.front = None
		self.rear = None

	def enqueue(self, data):
		temp = Node(data)

		if self.front == None and self.rear == None:
			self.front = temp
			self.rear = temp
		else:
			self.rear.next = temp
			self.rear = temp

	def dequeue(self):
		temp = self.front
		self.front = temp.next
		del temp


	def display(self):
		temp = self.front

		while temp:
			print(temp.data)
			temp = temp.next


linkque = Linked()

linkque.enqueue(4)
linkque.enqueue(5)
linkque.enqueue(6)
linkque.enqueue(7)

linkque.display()

linked.dequeue()



