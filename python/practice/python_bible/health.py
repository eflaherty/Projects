import random

health = 50

difficulty = 3 # easy mode, 2 is medium, 3 is hard

potion_health = int(random.randint(25, 50) / difficulty)
print(potion_health)

health = health + potion_health
print(health)