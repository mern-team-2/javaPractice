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




#  === check balancing of brackekts using stack === 

def check_bracket(string):

	open_br = ['(', '[', '{']
	close_br = [')', ']', '}']

	for i in range(len(string)):
		if string[i] in open_br:
			stack_1.add(string[i])

		elif string[i] in close_br:
			x = string[i]
			posi = close_br.index(x)

			if stack_1 is not None and open_br[posi] == stack_1.peek():
				stack_1.remove()
			
			else:
				print("unbalanced")




text = "{(my name is superman, who are you)({ fuck off??})[you fuck offf///.]}"
check_bracket(text)

if stack_1.stack is None:
	print("balanced brackets!")