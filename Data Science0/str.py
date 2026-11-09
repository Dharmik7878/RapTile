str = """This is a multi-line string.
aa jao strik rate ke divano,
final ki sham king mood me aya hai
virat ke bat se virasat pe mohor,
kabhi trophy pe gumnami thi, aj RCB ki manmani hai,
"""

print(str)

print("----------------------------------------------------------------------------------------------------------")

name = 'Raptile'

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])

print("----------------------------------------------------------------------------------------------------------")

print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])
print(name[-6])
print(name[-7])

print("----------------------------------------------------------------------------------------------------------")

print(name[0:3])
print(name[3:7])
print(name[2:-1])

print("----------------------------------------------------------------------------------------------------------")

h = "Hello, World! 7818"

print(len(h))
print(h.upper())
print(h.lower())
print(h.capitalize())
print(h.title())
print(h.replace("World", "Python"))
# rstrip
# lstrip
# strip
print(h.find("o"))
print(h.split(","))
print(h.isalpha())
print(h.isdigit())
print(h.isalnum())
print(h.isspace())
print(h.count("8"))

print("----------------------------------------------------------------------------------------------------------")

template = "My name is {} and I am {} years old."
iam = "dhamo"
my_age = 22
temp = template.format(iam, my_age)

print(temp)
# print(template.format("dhamo", 22))

print("----------------------------------------------------------------------------------------------------------")

l = [1, 2, 3, 4, 5]

ft, *a, lt = l

print(l)
print(ft)
print(a)
print(lt)