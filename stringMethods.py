firstName = "sam"
secondName = "davIes"

# String length
print("Lenght of " + firstName + " is " + str(len(firstName)))
print("Lenght of " + secondName + " is " + str(len(secondName)))

# Finding the position of a certain char in a string
print("Position of letter d,a,v in davies")
print(secondName.find("d"))
print(secondName.find("a"))
print(secondName.find("v"))

# Capitalise
print(firstName.capitalize() + " " + secondName.capitalize())

# All upper
print(firstName.upper())

# All lower
print(secondName.lower())

# Is digit
print(firstName.isdigit())

# is alpha, if is only letters
print(firstName.isalpha())

# Count, letters in a string
print("Letters of 's' in " + firstName + " = " + str(firstName.count("s")))