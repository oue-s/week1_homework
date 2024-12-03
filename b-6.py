import random

face = int(input("サイコロの面の数は？"))
count = int(input("何回振りますか？"))

result_saikoro = []
for i in range(count):
    result_saikoro.append(random.randint(1, face))

print(result_saikoro)
