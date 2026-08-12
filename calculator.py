def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

add=add(1,2)
print(add)

subtract=subtract(1,2)
print(subtract)

multiply=multiply(1,2)
print(multiply)

divide=divide(1,2)
print(divide)
