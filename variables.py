# Using varibales in python

# Strings
# Use either "" or ''
print("###   STRINGS   ###")
firstName = "Sam"
secondName = 'Davies'
fullName = firstName + " " + secondName
# Can check type of variable using type
print(type(firstName))
print("Hello " + fullName)

# New Line
print("\n")

# Intergers
print("###   INTEGERS   ###")
x = 5
y = 3
z = x + y
print(type(z))
# Type casting
print(str(x) + " + " + str(y) + " = " + str(z))

# New Line
print("\n")

# Floats
print("###   FLOATS   ###")
x = 2.5
y = 4.7
z = x + y
print(type(z))
# Type casting
print(str(x) + " + " + str(y) + " = " + str(z))

# New Line
print("\n")

# Boolean
print("###   BOOLEANS   ###")
x = True
print(type(x))
# Type casting
print("x is " + str(x) + " and the opposite of x is " + str(not x))