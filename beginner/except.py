# try:
#     x = int(input("Enter a number: "))
#     y = int(input("Enter another number: "))
#     print(x / y)  # This will raise an exception if y is zero
# except ValueError:
#     print ("Please enter a valid number next time!")
# except ZeroDivisionError:
#     print ("Cannot divide by zero!")
#     y = 1  # Default value to avoid division by zero
#     print("Using default value for y, division:", x/y)
# finally:
#     print("This block always executes, regardless of exceptions.")

########################
# def someFunc():
#     if True:
#         raise Exception("This is a custom exception message.")
    
########################
x = 100
y = 20
assert(x > y), "x should be greater than y, but it is not!"
print("Assertion passed, x is greater than y.")



