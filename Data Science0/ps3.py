fruits = []

f1 = "keri" # input("Enter a fruits: ")
f2 = "kela" # input("Enter a fruits: ")
f3 = "safarjan" # input("Enter a fruits: ")
f4 = "chiku" # input("Enter a fruits: ")
f5 = "narangi" # input("Enter a fruits: ")
f6 = "mosambi" # input("Enter a fruits: ")
f7 = "jamrukh" # input("Enter a fruits: ")

fruits.append(f1)
fruits.append(f2)
fruits.append(f3)
fruits.append(f4)
fruits.append(f5)
fruits.append(f6)
fruits.append(f7)

print(fruits)

print("--------------------------------------------------------------------------------------------------------------------")

marks = []

f1 = 1 # int(input("Enter a marks: "))
f2 = 2 # int(input("Enter a marks: "))
f3 = 3 # int(input("Enter a marks: "))
f4 = 4 # int(input("Enter a marks: "))
f5 = 5 # int(input("Enter a marks: "))
f6 = 6 # int(input("Enter a marks: "))
f7 = 7 # int(input("Enter a marks: "))

marks.append(f1)
marks.append(f2)
marks.append(f3)
marks.append(f4)
marks.append(f5)
marks.append(f6)
marks.append(f7)

print(marks)

print("--------------------------------------------------------------------------------------------------------------------")

l = (1, 2, 2, 3, 4, 5, 2, 2, 6, 7, 8, 9, 2, 2, 2)
print(sum(l))
print(len(l))
print(l.count(2))

print("--------------------------------------------------------------------------------------------------------------------")

# words = {
#     "madad": "Help",
#     "kursi": "Chair",
#     "billi": "Cat"
# }

# word = input("Enter the word you want meaning of: ")

# print(words[word])

print("--------------------------------------------------------------------------------------------------------------------")

# s = set()
# n = input("Enter number: ")
# s.add(int(n))  
# n = input("Enter number: ")
# s.add(int(n))  
# n = input("Enter number: ")
# s.add(int(n))  
# n = input("Enter number: ")
# s.add(int(n))  
# n = input("Enter number: ")
# s.add(int(n))  
# n = input("Enter number: ")
# s.add(int(n))  
# n = input("Enter number: ")
# s.add(int(n))  
# n = input("Enter number: ")
# s.add(int(n))  

# print(s)

print("--------------------------------------------------------------------------------------------------------------------")

sett = set()
sett.add(18)
sett.add("18")
sett.add(18.18)

print(sett)

print("--------------------------------------------------------------------------------------------------------------------")

d = {}

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

print(d)