class node:
	
	def __init__ (self, data):
		self.data = data
		self.next = None

class linkedList:

	def __init__ (self):
		self.head = None

	# def printList(self):
	# 	temp = self.head

	# 	while (temp):
	# 		print(temp.data)
	# 		temp = temp.next












# 	'''MAKING INDIVIDUAL NODES ''' 

# if __name__ == '__main__':
	
# 	list1 = linkedList()

# 	list1.head = node(1)

# 	second = node(2)
# 	third = node(3)

# 	list1.head.next = second;
# 	second.next = third;

# list1.printList()













	''' ADDING NODE AT THE BEGINNING '''

# list1 = linkedList()

# def insertlist(value):

# 	temp = node(value)
# 	temp.next = list1.head
# 	list1.head = temp 


# def printlist():
# 	temp = list1.head

# 	while(temp):
# 		print(temp.data)
# 		temp = temp.next


# def makeLinkedlist(num):
	
# 	for i in range(num):
# 		value = int(input("input.."))
# 		insertlist(value)
# 		printlist()


# num = int(input("how many numbers you want to print: "))
# makeLinkedlist(num)












	'''ADD A NODE AT nth POSITION'''



# list1 = linkedList()

# def insertlist(value, n):

# 	temp1 = node(value)
# 	temp1.next = None

# 	if(n==1):
# 		temp1.next = list1.head
# 		list1.head = temp1
# 		return

# 	temp2 = list1.head 
# 	for i in range(n-2):
# 		temp2 = temp2.next

# 	temp1.next = temp2.next 
# 	temp2.next = temp1


# def printlist():
# 	temp = list1.head

# 	while(temp):
# 		print(temp.data)
# 		temp = temp.next


# insertlist(2,1)
# insertlist(3,2)
# insertlist(4,1)
# insertlist(5,2)
# insertlist(8,3)

# printlist()









# 	DELETING A NODE AT nth POSITION

# list1 = linkedList()

# def insertlist(value):

# 	temp = node(value)
# 	temp.next = list1.head
# 	list1.head = temp 


# def deletelink(n):
# 	temp1 = list1.head 

# 	if(n==1):
# 		list1.head = temp1.next 
# 		del temp1
# 		return

# 	for i in range(n-2):
# 		temp1 = temp1.next 

# 	temp2 = temp1.next 
# 	temp1.next = temp2.next
# 	del temp2	

# def printlist():
# 	temp = list1.head

# 	while(temp):
# 		print(temp.data)
# 		temp = temp.next

# insertlist(3)
# insertlist(6)
# insertlist(5)
# insertlist(4)
# insertlist(2)

# printlist()

# num =  int(input("insert nTH number to delete: "))

# deletelink(num)

# printlist()









# 	REVERSING A LINKIED LIST (data will not change, only address change)



# list1 = linkedList()

# def insertlist(value):

# 	temp = node(value)
# 	temp.next = list1.head
# 	list1.head = temp 


# def printlist():
# 	temp = list1.head

# 	while(temp):
# 		print(temp.data)
# 		temp = temp.next


# # def reverslist():
# 	current = list1.head 
# 	prev = None

# 	while (current != None):
# 		next = current.next
# 		current.next = prev
# 		prev = current
# 		current = next

# 	list1.head = prev

# insertlist(3)
# insertlist(6)
# insertlist(5)
# insertlist(4)
# insertlist(2)

# printlist()

# reverslist()

# printlist()











# # 	PRINT LINKEDLIST BY RECCURSION IN FORWARD AND REVERSE ORDER


# list1 = linkedList()

# # #  add element at the beggining

# # def insertlist(value):
# # 	temp2 = node(value)
# # 	temp2.next = list1.head
# # 	list1.head = temp2




# #	add element at the end of list

# def insertlist(value):
# 	temp = node(value)
# 	temp.next = None

# 	if list1.head == None:
# 		list1.head = temp
# 	else:
# 		temp1 = list1.head 
# 		while temp1.next != None :
# 			temp1 = temp1.next
# 		temp1.next = temp



# def printlist(temp):
# 	if temp == None:
# 		return

# 	print(temp.data)
# 	printlist(temp.next)
	


# insertlist(3)
# insertlist(6)
# insertlist(5)
# insertlist(4)
# insertlist(2)



# printlist(list1.head)














list1 = linkedList()

def insertlist(value):
	temp = node(value)
	temp.next = None

	if list1.head == None:
		list1.head = temp
	else:
		temp1 = list1.head 
		while temp1.next != None:
			temp1 = temp1.next
		temp1.next = temp

def printlist():
	temp = list1.head

	while temp != None:
		print(temp.data)
		temp = temp.next


def recreverslist(p):

	if p.next == None:
		list1.head = p
		return

	recreverslist(p.next)
	temp= p.next
	temp.next = p
	p.next = None


	

insertlist(3)
insertlist(6)
insertlist(5)
insertlist(4)
insertlist(2)

printlist()

p = list1.head 

recreverslist(p)

printlist()
