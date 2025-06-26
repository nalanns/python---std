n = 5
fact = 1
while n> 1:
    fact *= n
    n -= 1
    
print(fact)


def factorial(n):
    if n < 1:
        return 1
    else:
        number = factorial(n - 1) * n
        return number 
        
        
        
        
        
        
        
    