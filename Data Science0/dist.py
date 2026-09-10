comp_car = {
    "tata": 800000,
    "mahindra": 1500000,
    "maruti":  500000,
    "rangerover": 10000000,
    "toyota": 4000000,
}

print(comp_car, type(comp_car))

s = set()
st = {1, 4, 5, 5, 5, 6, 7, 8, 9, 10}
print(st, len(st))
st.remove(10)
print(st)

s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(s)

print(s.union(st))
print(s.intersection(st))

