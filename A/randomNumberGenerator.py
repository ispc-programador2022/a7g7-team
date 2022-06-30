import random

def genrnd():
    randomList = []
    for num in range(0,50):
        randomList.append(random.randint(0,1000))
    return randomList
