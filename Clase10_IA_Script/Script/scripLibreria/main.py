import random
librer = {}
numero = random.randint(0,1000)
librer[0] = []
for i in range(len(librer)+1):
    librer[i] = random.randint(0,1000)

print(librer)