# def helloworld():
#     print("Hello, World!")
    
# helloworld()    # This function prints "Hello, World!" to the console

# def add(x,y):
#     return x + y  # This function returns the sum of x and y
# result = add(5, 3)  # Calling the add function with arguments 5 and 3
# print(result)  # This prints the result of the addition, which is 8 


def mysum(*numbers):
    result = 0
    for num in numbers:
        result += num
    return result 

print(mysum(10,20,40,54))


