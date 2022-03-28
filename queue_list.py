##      simple List method

class Stack:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        else:
            return self.queue.pop(0)

    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)


questack = Stack()

questack.enqueue(5)
questack.enqueue(6)
questack.enqueue(7)

questack.dequeue()

questack.enqueue(8)

questack.display()














##       cercular List or Array method

# class Stack:
#     def __init__(self, N =10):
#         self.N= N
#         self.queue = [None] * N
#         self.front = -1
#         self.rear = -1

#     # def is_empty(self):
#     #     if self.front == -1 and self.rear == -1:
#     #         True
#     #     else:
#     #         False

#     def en_queue(self, data):

#         if (self.rear+1)%self.N == self.front:
#             print("queue is full")
#             return

#         elif self.front == -1 and self.rear == -1:
#             self.front = self.rear = 0

#         else:
#             self.rear = (self.rear+1)%self.N

#         self.queue[self.rear] = data 

#     def de_queue(self):
#         if self.front == -1 and self.rear == -1:
#             return

#         elif self.front == self.rear:
#             self.front = self.rear = -1

#         else:
#             self.front = (self.front+1)%self.N

#     def print_que(self):
#         for i in range(self.N):
#             print(self.queue[i])


# questack = Stack()

# questack.en_queue(12)
# questack.en_queue(23)
# questack.en_queue(34)
# questack.en_queue(45)
# questack.en_queue(56)
# questack.en_queue(67)
# questack.en_queue(78)
# questack.en_queue(56)
# questack.en_queue(67)
# questack.en_queue(78)
# questack.de_queue()
# questack.en_queue(56)



# questack.print_que()