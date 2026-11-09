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
        print("Invalid operation")