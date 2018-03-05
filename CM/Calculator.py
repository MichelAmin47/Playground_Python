# while loop

x = 1

while x <= 10:
    print x
    x = x+1

# for loop

for numberOne in range(1, 11):
    print(numberOne)
# welke is veiliger?

# calculator
for numberOne in range(1,11):
    for numberTwo in range(1,11):
        print(str(numberOne) + " x " + str(numberTwo) + " = " + str(numberOne * numberTwo))
    print("")
