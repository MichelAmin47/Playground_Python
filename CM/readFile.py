# open a file and read all
with open('python.txt') as fp:
    for line in fp:
        print line

# open file and check content
with open('python.txt') as fp:
    for line in fp:
        if "kurkentrekkers" in line:
            print ("word found")


# open file and check content and return place
with open('python.txt') as fp:
    print(type(fp))
    for line in fp:
        print line.find("kurkentrekkers")


# open file, check content and return place. Proper


