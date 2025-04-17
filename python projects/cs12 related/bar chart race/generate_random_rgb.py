import random

uniqueitems = ['apple', 'orange', 'banana', 'blueberry', 'strawberry', 'kiwi', 'rasberry']

def rand_rgb():
    rgb = (random.randint(0,225), random.randint(0,225), random.randint(0,225))
    return rgb

rgb = []
#apply to amount of unique items
for i in range(len(uniqueitems)):
    rgb.append(rand_rgb())

print(rgb)