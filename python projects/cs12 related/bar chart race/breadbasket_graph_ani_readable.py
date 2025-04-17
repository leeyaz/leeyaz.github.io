import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ogdf = pd.read_csv(r"bar chart race/BreadBasket_DMS_shortened.csv") #reads csv

#Get rid of useless data (Value == NONE, drop)
df = ogdf[~(ogdf['Item'] == 'NONE')]

fig, ax = plt.subplots() #to access more graph editing methods
fig.set_size_inches(6.8, 5) #size of graph
fig.subplots_adjust(left=0.25, right=0.95, top=0.90, bottom=0.15) #padding to prevent cutoff

dates = []
#sort to only unique dates
for i in df["Date"].unique():
    dates.append(i)
#for each unique date, append all items for that day in a list
alldays = {} #see line 27
for day in dates:
    for1day = []
    onedayitems = df.loc[df["Date"] == day,"Item"] #this will return scalar indexes of the items for that day
    for key in onedayitems:
        for1day.append(key) #use indexes got from line 24 to append items for1day
    alldays[day] = for1day #for dict alldays, key=date (str), value=items that day (list)
#print(alldays)

#gen random rgb (hex code doesn't work? difficulty generating one that works)
def rand_rgb(): #returns rgb values (random, type=tuple)
    return (random.randint(0,255)/255, random.randint(0,255)/255, random.randint(0,255)/255)
rgb = []
#have a rgb tuple for the number of unique items
for i in range(len(df["Item"].unique())):
    rgb.append(rand_rgb())
colordict = {item: rgb[i] for i, item in enumerate(df['Item'].unique())} #a color(aka rgb tuple) attributed to each item in a dictionary

#for each value(type=list) for each date (func param), find uniqueitems and itemcount to make a graph
def update(date):
    ax.clear()
    grocery = alldays.get(date) #items for one day (type=list)
    uniqueitems, itemcount = np.unique(grocery, return_counts=True) #x and y values
    sorting = itemcount.argsort() #sort according to itemcount (ascending) line 45 & 46
    uniqueitems = uniqueitems[sorting]
    itemcount = itemcount[sorting]

    #show first 10 only
    head_uniqueitems = uniqueitems[-10:] #since both arrays are ascending, count backwards from highest index
    head_itemcount = itemcount[-10:]
    ax.barh(y=head_uniqueitems, height=0.5, width=head_itemcount, 
            color = [colordict[item] for item in head_uniqueitems]) #for each item in head_uniqueitems, get the colour from colordict based on name of the item
    #text values
    for index, value in enumerate(head_itemcount):
        plt.text(value, index-0.1, str(value)) #(x=value(aka length), y=index 0-9 counting downwards from top)
    #updatable chart items
    plt.title(f"items to frequency on {date}", fontsize=10)
    ax.set_xticks(range(max(head_itemcount)+1)[::2]) #ticks jump by two all the way to max head_itemcount
    ax.set_xticklabels(range(max(head_itemcount)+1)[::2]) #+1 because range counts non inclusive in the end
    #bar chart customization axes labels
    ax.set_xlabel("frequency")
    ax.set_ylabel("items")
    ax.yaxis.set_label_coords(-0.29, 0.5) #to stop the ylabel from moving w/ the animation


chart_animation = animation.FuncAnimation(fig, update, frames=[a for a in alldays], repeat=False, interval=1000) #frames are the params of update
chart_animation.save('bar chart race/breadbasket_animation.gif', writer = 'pillow', fps = 6) #pillow writes gifs
plt.show()