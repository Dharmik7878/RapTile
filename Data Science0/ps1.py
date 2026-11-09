num = -1#int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

print("----------------------------------------------------------------------------------------------------------")

age = 19#int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

print("----------------------------------------------------------------------------------------------------------")

number = 5#int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")    
else:
    print("The number is odd.")

print("----------------------------------------------------------------------------------------------------------")

week = 3#int(input("Enter a number (1-7) representing the day of the week: "))

match week:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid input. Please enter a number between 1 and 7.")

print("----------------------------------------------------------------------------------------------------------")

n1 = 10#int(input("Enter the first number: "))
n2 = 20#int(input("Enter the second number: "))

operation = "+"#input("Enter the operation (+, -, *, /): ")

match operation:
    case "+":
        print("Result:", n1 + n2)
    case "-":
        print("Result:", n1 - n2)
    case "*":
        print("Result:", n1 * n2)
    case "/":
        if n2 != 0:
            print("Result:", n1 / n2)
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation. Please enter one of the following: +, -, *, /.")

print("----------------------------------------------------------------------------------------------------------")

i = 5#int(input("enter the number : "))

for i in range(1, 11):
    print(i, "x", i, "=", i * i)

print("----------------------------------------------------------------------------------------------------------")

# sum = 0

# for i in range(1, 101):
#     print(i)
#     sum += i

# print("The sum of 1 to 100 is:", sum)

print("----------------------------------------------------------------------------------------------------------")

for i in range(1, 6):
    print("*" * i)

print("----------------------------------------------------------------------------------------------------------")

s = 0
d = 1

while d <= 100:
    s += d
    d += 1

print("The sum of 1 to 100 is:", s)

print("----------------------------------------------------------------------------------------------------------")

password = "superman#7878"
entered_pass = "superman#7878"#input("Enter the password: ")

while entered_pass != password:
    print("Incorrect password. Try again.")
    entered_pass = input("Enter the password: ")

print("Access granted. Welcome!")

print("----------------------------------------------------------------------------------------------------------")

r_num = 12345

print(int(str(r_num)[::-1]))

print("----------------------------------------------------------------------------------------------------------")

for i in range(1, 11):
    if i == 5:
        break
    print(i)

print("----------------------------------------------------------------------------------------------------------")

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

print("----------------------------------------------------------------------------------------------------------")

for i in range(1, 6):
    match i:
        case 1:
            print(1)
        case 2:
            print(2)
        case 3:
            pass
        case 4:
            print(4)
        case 5:
            print(5)