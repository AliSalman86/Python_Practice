# numeric type => int:
# decimal:
print(5)
# binary
print(0b10)
# octal
print(0o10)
# hexa
print(0x10)

# int constructor to convert numeric types to int:
print(int(3.5))
print(int(-3.5))
print(int("300"))
print(int("10000", 3))
print("This is an octal value \v 10")

# collections: str, bytes, list, and dict

c = 'Oslo is beautiful and'
print(c.islower())

print(c.__add__(' is Great'))

print(c.__contains__('beautiful'))

print(c.__eq__('Oslo is beautiful and'))

# lists, string of objects which is mutable
myList = [1, 2, 3, 4]
print(len(myList))

myList.append(5)
print(myList)
