<<<<<<< HEAD
age = int(input("Enter your age: "))
month = int(input("Enter the month number (1-12): "))
table_num = int(input("Enter a number to print its multiplication table: "))
print("----------------------------------------------------------------------------------------------------")
if(age >= 21):
    print("You are eligible to vote, drive and get married.")
elif(age >= 20):
    print("You are eligible to vote or drive, but not eligible for marriage.")
elif(age >= 18):
    print("You are eligible to vote or drive.")
else:
    print("You are not eligible to vote or drive.")

print("----------------------------------------------------------------------------------------------------")
match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Invalid month number. Please enter a number between 1 and 12.")

print("----------------------------------------------------------------------------------------------------")
for i in range(0, 10):
    if i % 2 == 0:
        print(i, "is even.")
    else:
        print(i, "is odd.")

print("----------------------------------------------------------------------------------------------------")
for i in range(1, 11):
    print(table_num, "*", i, "=", table_num * i)

print("----------------------------------------------------------------------------------------------------")
i = 1
while i < 6:
    print(i)
    i += 1

=======
age = int(input("Enter your age: "))
month = int(input("Enter the month number (1-12): "))
table_num = int(input("Enter a number to print its multiplication table: "))
print("----------------------------------------------------------------------------------------------------")
if(age >= 21):
    print("You are eligible to vote, drive and get married.")
elif(age >= 20):
    print("You are eligible to vote or drive, but not eligible for marriage.")
elif(age >= 18):
    print("You are eligible to vote or drive.")
else:
    print("You are not eligible to vote or drive.")

print("----------------------------------------------------------------------------------------------------")
match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Invalid month number. Please enter a number between 1 and 12.")

print("----------------------------------------------------------------------------------------------------")
for i in range(0, 10):
    if i % 2 == 0:
        print(i, "is even.")
    else:
        print(i, "is odd.")

print("----------------------------------------------------------------------------------------------------")
for i in range(1, 11):
    print(table_num, "*", i, "=", table_num * i)

print("----------------------------------------------------------------------------------------------------")
i = 1
while i < 6:
    print(i)
    i += 1

>>>>>>> 0be82eea013b4a95ecf7d92f4bd55fb50d4253d3
print("----------------------------------------------------------------------------------------------------")