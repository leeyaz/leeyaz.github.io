import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ogdf = pd.read_csv(r"bar chart race/BreadBasket_DMS_shortened.csv")

#Get rid of useless data (Value == NONE, drop)
df = ogdf[~(ogdf['Item'] == 'NONE')]

fig, ax = plt.subplots()

dates = []
#sort to only unique dates
for i in df["Date"].unique():
    dates.append(i)
#for each unique date, append all items for that day in a list
alldays = {}
for day in dates:
    for1day = []
    onedayitems = df.loc[df["Date"] == day,"Item"]
    for key in onedayitems:
        for1day.append(key)
    alldays[day] = for1day #for dict alldays, key=date (str), value=items that day (list)
#print(alldays)

#gen random rgb (hex code doesn't work??????)
def rand_rgb():
    rgb = (random.randint(0,225)/225, random.randint(0,225)/225, random.randint(0,225)/225)
    return rgb
rgb = []
#apply to amount of unique items
for i in range(len(df["Item"].unique())):
    rgb.append(rand_rgb())
colordict = {item: rgb[i] for i, item in enumerate(df['Item'].unique())} #a color attributed to each item

#bar chart customization
ax.set_xlabel("frequency")
ax.set_ylabel("items")

#for each value(type=list) for each date (func param), find uniqueitems and itemcount to make a graph
def update(date):
    ax.clear()
    grocery = alldays.get(date)
    uniqueitems, itemcount = np.unique(grocery, return_counts=True) #x and y values
    sorting = itemcount.argsort() #sort according to itemcount (ascending)
    uniqueitems = uniqueitems[sorting]
    itemcount = itemcount[sorting]

    #show first 10 only
    head_uniqueitems = uniqueitems[-10:] #since both arrays are ascending, count backwards from highest index
    head_itemcount = itemcount[-10:]
    ax.barh(y=head_uniqueitems, height=0.5, width=head_itemcount, color = [colordict[item] for item in head_uniqueitems])
    #text values
    txt_value_axis = []
    for index, value in enumerate(head_itemcount):
        plt.text(value, index-0.1, str(value))
        txt_value_axis.append(value)
    #updatable chart items
    plt.title(f"items to frequency on {date}", fontsize=10)
    ax.set_xticks(range(max(head_itemcount)+1)[::2])
    ax.set_xticklabels(range(max(head_itemcount)+1)[::2])

chart_animation = animation.FuncAnimation(fig, update, frames=[a for a in alldays], repeat=False, interval=1000)
chart_animation.save('breadbasket_animation.gif', writer = 'pillow', fps = 3)
plt.show()