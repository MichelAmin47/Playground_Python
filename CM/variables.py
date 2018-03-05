# create first var
myName = "Michel"

print(myName)

print("My name is: " + myName)


# int
age = 35

print(age)

# print("My age is " + age)

print("My age is " + str(age))


# float
bla = 1.7

print(bla)

print("My bla is: " + str(bla))


# boolean

presentInClassRoom = True

print(presentInClassRoom)

print("I'm present in the classroom: " + str(presentInClassRoom))


# if statement + indent
if presentInClassRoom:
    print("I'm here!")

if presentInClassRoom:
    print("I'm here!")
else:
    print("Not here")
print("indent")

# Wrong!
if not presentInClassRoom:
    print("I'm here!")
else:
    print("Not here")

if age > 29:
    print("OUDDD!")
else:
    print("broekie!")
