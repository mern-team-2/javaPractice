class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        else:
            return self.queue.pop(0)

    def front(self):
    	if self.queue is None:
    		return
    	else:
    		return self.queue[0]
    	

    def size(self):
        return len(self.queue)


def levelOrder(root):
	if root is None:
		return

	que = Queue()
	que.enqueue(root)

	while (que.size()) != 0:
		current = que.front()
		print(current.data)
		if current.left != None: que.enqueue(current.left)
		if current.right != None: que.enqueue(current.right)
		que.dequeue()


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.righ = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

levelOrder(root)

