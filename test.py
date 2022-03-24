import random

usr = input("Please Enter a String : ")

result = ""
key = ""

for i in usr:
    x = ord(i)
    y = x + random.randint(100, 300)
    z = chr(y)
    result = result + z
print(result)