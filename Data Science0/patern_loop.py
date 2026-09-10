# n = int(input("Enter a number: "))

# for i in range(1, n + 1):
#     if i == 1 or i == n:
#         print("*" * n, end="")
#     else:
#         print("*", end="")
#         print(" " * (n - 2), end="")
#         print("*", end="")
#     print("")
    
# for i in range(1, 11):
#     print(f"{n} x {11 - i} = {n * (11 - i)}")

class employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")
        
    def __str__(self):
        return f"Employee(Name: {self.name}, Age: {self.age}, Salary: {self.salary})"
    
    def __repr__(self):
        return f"employee('name: {self.name}'\nage: {self.age} \nsalary: {self.salary})"
    
    def __len__(self):
        return len(self.name)

emp = employee("John Doe", 30, 50000)
emp.display()
print(str(emp))
print(repr(emp))
print(len(emp))