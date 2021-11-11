import random
import os
import timeit
random.seed()

"""   
f = open("timing1.text", "w")
while os.path.getsize('timing1.text') < 52428800:
    f.write('123456789987654321123456789987654321\n')
"""


data1 = """
s1 = 0
with open ("timing1.text", "r") as file: 
    for line in file: 
        if line.strip().isdigit():
            s1 += int(line.strip())
"""

data2 = """
with open ("timing1.text", "r") as file: 
    x = (int(line.strip())for line in file if line.strip().isdigit())
    s2 = sum(x)


"""

data3 = """
s3 = 0
with open ("timing1.text", "r") as file: 
    text = file.readlines()
    for line in text:
        if line.strip().isdigit():
            s3  += int(line.strip())
"""
print(timeit.timeit(data1, number = 10))
print(timeit.timeit(data2, number = 10))
print(timeit.timeit(data3, number = 10))
