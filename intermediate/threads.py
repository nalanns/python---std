import threading
import time

# def helloworld():
#     print("Hello, World!")
    
# t1 = threading.Thread(target=helloworld) 
# t1.start()  # Start the thread 

# def func1():
#     for i in range(5):
#         print(f"Function 1: {i}")
# def func2():
#     for i in range(5):
#         print(f"Function 2: {i}")
# # Create threads for each function
# t1 = threading.Thread(target=func1)     
# t2 = threading.Thread(target=func2)
# # Start the threads
# t1.start()
# t2.start()
 
 
# def hello():
#     for i in range(50):
#         print("hello")
    
# t1 = threading.Thread(target=hello)
# t1.start()  # Start the thread

# print("Main thread is running...")
# # Wait for the thread to finish


####################################
# x = 8192
# lock = threading.Lock()

# def double():
#     global x, lock
#     lock.acquire()  # Acquire the lock to ensure thread safety
#     while x<16384 :
#         x *= 2
#         print(x)
#         time.sleep(1)
#     print("Thread finished doubling x to:", x)
#     lock.release()  # Release the lock after finishing
# def halve():
#     global x, lock
#     lock.acquire()  # Acquire the lock to ensure thread safety
#     while x > 1:
#         x /= 2
#         print(x)
#         time.sleep(1)
#     print("Thread finished halving x to:", x) 
#     lock.release()  # Release the lock after finishing
# # Create threads for doubling and halving
# t1 = threading.Thread(target=double)
# t2 = threading.Thread(target=halve)
# # Start the threads

# t2.start()
# t1.start()

###################################
semaphore = threading.BoundedSemaphore(value=5)  # Limit to 5 concurrent threads 

def access(thread_number):
    print(f"Thread {thread_number} is trying to access")
    semaphore.acquire()  # Acquire the semaphore
    print(f"Thread {thread_number} has accessed")
    time.sleep(10)  # Simulate some work
    print(f"Thread {thread_number} is releasing access")
    semaphore.release()  # Release the semaphore
    
for thread_number in range(1, 11):
    t = threading.Thread(target=access, args=(thread_number,))
    t.start()  # Start the thread
    time.sleep(1)  # Slight delay to allow threads to start in sequence
    
    

 
