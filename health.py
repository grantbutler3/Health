import random

health = 50

difficulty = 1

random.randint(10,20)

potion_health = int(random.randint(25,50) / difficulty)

health = health + potion_health

print(health)