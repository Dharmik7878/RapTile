<<<<<<< HEAD
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
    
print("Select operation:\n1. + for Addition\n2. - for Subtraction\n3. * for Multiplication\n4. / for Division\n")

o = input("Enter operation: ")
    
match o:
    case "+":
        print(f"Result: {a + b}")
    case "-":
        print(f"Result: {a - b}")
    case "*":
        print(f"Result: {a * b}")
    case "/":
        print(f"Result: {a / b}")
    case _:
=======
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
    
print("Select operation:\n1. + for Addition\n2. - for Subtraction\n3. * for Multiplication\n4. / for Division\n")

o = input("Enter operation: ")
    
match o:
    case "+":
        print(f"Result: {a + b}")
    case "-":
        print(f"Result: {a - b}")
    case "*":
        print(f"Result: {a * b}")
    case "/":
        print(f"Result: {a / b}")
    case _:
>>>>>>> 0be82eea013b4a95ecf7d92f4bd55fb50d4253d3
        print("Invalid operation")