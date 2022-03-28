class Node:
	
	def __init__(self, data):
		self.data = data 
		self.next = None

class linkedList:
	
	def __init__(self):
		self.head = None
		
		





list1 = linkedList()

def insertlist(value):
	temp = Node(value)
	temp.next = None

	if list1.head == None:
		list1.head = temp
	else:
		temp1 = list1.head 
		while temp1.next != None:
			temp1 = temp1.next
		temp1.next = temp

def print_list():
	temp = list1.head

	while temp != None:
		print(temp.data)
		temp = temp.next



# === method:1 	middle element by traverse linked list ===  

# def middle_element():
# 	count = 0
# 	temp = list1.head 
# 	while temp.next != None:
# 		temp = temp.next
# 		count += 1

# 	halfcount = count/2

# 	temp1 = list1.head
# 	for i in range(halfcount):
# 		temp1 = temp1.next
# 	return temp1.data




# 	=== method:2 middle eliment by traverse 2 linked list at same time, one is normal and other is 2x fast

def middle_element():
	slow_node = list1.head 
	fast_node = list1.head 

	while fast_node.next != None:
		fast_node = fast_node.next.next
		slow_node = slow_node.next
	return slow_node.data




insertlist(11)
insertlist(12)
insertlist(13)
insertlist(14)
insertlist(15)
insertlist(16)
insertlist(17)


print_list()

data = middle_element()

print("middle string" , data)
