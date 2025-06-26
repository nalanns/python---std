import threading
import time

# event = threading.Event()
# def myfunction():
#     print("Waiting for event to be set...\n")
#     event.wait()  # This will block until the event is set
#     print("Event is set, continuing execution") 
    
    
    
# t1 = threading.Thread(target=myfunction)
# t1.start()

# x = input("Do you want to trigger the event? y/n\n")  # Wait for user input
# if x == "y":
#     event.set()  # This will unblock the thread waiting on the event
# else:  
#     print("Event not set, thread will remain blocked.")

####################################
path = "text.txt"
text = ""
def readFile():
    global path, text
    while True:
        with open(path, "r") as file:
            text = file.read()
        time.sleep(3) 
        
        
def printLoop():
    for x in range(30):
        print(text)
        time.sleep(1)
        
        
t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=printLoop)
t1.start()
t2.start()


