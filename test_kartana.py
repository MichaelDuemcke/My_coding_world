#kartana
# link : https://www.codewars.com/kata/5a20eeccee1aae3cbc000090/train/python
#necessary modules
import random
from array import array

#INPUT
# first generating the tile

nField0 = [


    ]


n = random.randint(0, 2)
i = 0
nField1 = []
for generatingField1 in range(0, 3, 1):
    nField1.insert(n, i)
    i = i + 1
nField0.append(nField1)
nField2 = []
for generatingField2 in range(3, 6, 1):
    nField2.insert(n, i)
    i = i + 1
nField0.append(nField2)
nField3 = []
for generatingField3 in range(6, 9, 1):
    nField3.insert(n, i)
    i = i + 1
nField0.append(nField3)
print(nField0)

# this a test section
















