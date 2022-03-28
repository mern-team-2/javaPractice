# 	stack using List 

class Stack:

	def __init__(self):
		self.stack = []


	def add(self, data):
		# if data not in self.stack:
		self.stack.append(data)


	def peek(self):
		return self.stack[-1]


	def remove(self):
		if len(self.stack) <= 0:
			print("stack is empty")
		else:
			self.stack.pop()


stack_1 = Stack()




# # 	=== reverse string using stack ===


# def reverse_string(string):
# 	for i in range(len(string)):
# 		stack_1.add(string[i])

# 	for i in range(len(string)):
# 		print(stack_1.peek())
# 		stack_1.remove()







# stack_1.add(12)
# stack_1.add(13)
# stack_1.add(14)
# stack_1.add(15)
# stack_1.add(15)
# stack_1.remove()

# print(stack_1.peek())



# text = "hello"
# reverse_string(text)

		