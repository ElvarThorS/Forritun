a = bool(int(input("A")))
b = bool(int(input("B")))
c = bool(int(input("C")))

d = int((a and not b)or(not b and c))
# compute d

print("D is", d)