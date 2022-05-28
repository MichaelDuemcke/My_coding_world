import random
# this is a section to test other ideas

def myfunction():
    print("Hello")
    return 0.1


nField0 = [


]
listOfNumbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(listOfNumbers, )

n = random.randrange(0, 8, 1)
i = 0
nField1 = []
for generatingField1 in range(0, 3, 1):
    nField1.insert(n, listOfNumbers)
    i = i + 1
nField0.append(nField1)
nField2 = []
for generatingField2 in range(3, 6, 1):
    nField2.insert(n, listOfNumbers)
    i = i + 1
nField0.append(nField2)
nField3 = []
for generatingField3 in range(6, 9, 1):
    nField3.insert(n, listOfNumbers)
    i = i + 1
nField0.append(nField3)
print(nField0)
