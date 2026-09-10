a = 78
b = 19
c = 3

avg = (a + b + c) / 3
print("Average:", avg)

print("----------------------------------------------------------------------------------------------------")

name = "dharmik"  # input("Enter your name: ")

def greet(name):
    r = (f"Hello, {name}! Welcome to the world of Python programming.")
    return r

greeting = greet(name)
print(greeting)

print("----------------------------------------------------------------------------------------------------")

def add(a, b):
    c = a + b
    return c

result = add(5, 7)
print("The sum is:", result)
    
print("----------------------------------------------------------------------------------------------------")
# lembda function

square = lambda x: x ** 2
print("Square of 5 is:", square(5))


print("----------------------------------------------------------------------------------------------------")