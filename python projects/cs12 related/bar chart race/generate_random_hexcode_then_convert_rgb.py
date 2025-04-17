import random

uniqueitems = ['apple', 'orange', 'banana', 'blueberry', 'strawberry', 'kiwi', 'rasberry']

#random hex code
def random_color():
    hex_color = str(hex(random.randint(0, 16777215)))
    return "#" + hex_color[2:]

#make list of colors for amount of unique items (why do i need a dict?)
item_colors = []
for i in range(len(uniqueitems)):
    item_colors.append(random_color())
print(item_colors)

def hex_to_rgb(hex):
  return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

rgb = []
for i in range(len(item_colors)):
   item_colors[i] = item_colors[i].replace("#", "")
   rgb.append(hex_to_rgb(item_colors[i]))

print(rgb)