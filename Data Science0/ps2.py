name = "dhamo"

print(name[0])
print(name[4])
print(len(name))

print("----------------------------------------------------------------------------------------------------")

str1 = "Raptile"
str2 = "Music"

print(str1 + " " + str2)
print(str1, str2)

print("----------------------------------------------------------------------------------------------------")

text = "pyhton programming"
text1 = " pyhton programming "

print(text[0:6])
print(text[-6:])
print(text[::2])
print(text1.strip())
print(text1.title())
print(text1.count("o"))

print("----------------------------------------------------------------------------------------------------")

an = "123abc"

if an.isalnum():
    print("The string is alphanumeric.")
else:
    print("The string is not alphanumeric.")

print("----------------------------------------------------------------------------------------------------")

n = "dhamo" #input("Enter name: ")
age = 22 #int(input("Enter age: "))

print(f"my name is {n} and i am {age} years old.")

sentence = "I am learning py programming."
new = sentence.replace("py", "python")
print(new)
print(sentence.index("py"))

sum = 0
vowels = ['a', 'e', 'i', 'o', 'u']
for char in sentence.lower():
    if char in vowels:
        sum += 1
print(f"Number of vowels in the sentence: {sum}")

pel = "madamd"

if pel == pel[::-1]:
    print(f"{pel} is a palindrome.")
else:
    print(f"{pel} is not a palindrome.")
    
print("----------------------------------------------------------------------------------------------------")