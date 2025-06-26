import queue

# q = queue.Queue()

# numbers = [10, 20, 30, 40, 50, 60, 70]
# for number in numbers:
#     q.put(number)  # Add numbers to the queue
    
# print(q.get())  # Get the first item from the queue
# print(q.get())  # Get the 2nd item from the queue 

#################################LIFO##########################
# q = queue.LifoQueue()

# numbers = [1, 2, 3, 4, 5, 6]
# for x in numbers:
#     q.put(x)  # Add items to the queue
# print(q.get())  # Get the last item from the queue
# print(q.get())  # Get the 2nd last item from the queue

##################################Priority Queue##########################
q = queue.PriorityQueue()

q.put((2, "hello")) # Add an item with priority 2
q.put((11, 99))
q.put((5, 7.5))
q.put((1, True))  # Add an item with priority 1

while not q.empty():
    #print(q.get())  # Get items in order of priority
    print(q.get()[1])  # Get only the second element of each tuple 


