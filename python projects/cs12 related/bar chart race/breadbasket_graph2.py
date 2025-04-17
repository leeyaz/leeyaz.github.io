# Import your code from the previous exercise
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ogdf = pd.read_csv(r"./BreadBasket_DMS_shortened.csv")

#Get rid of unused data
df = ogdf.drop(["Time", "Transaction"], axis=1) #i'm not even sure if this is needed lol

dates = []
#sort to only unique dates (that are indexes?)
for i in df["Date"].unique():
    dates.append(i)
#for each unique date, append all the subsequent Items in a list
alldays = {}
for day in dates:
    for1day = []
    onedayitems = df.loc[df["Date"] == day,"Item"]
    for index, value in enumerate(onedayitems):
        for1day.append(value)
    alldays[day] = for1day
print(alldays)

#gen random rgb (hex code doesn't work??????)
def rand_rgb():
    rgb = (random.randint(0,225)/225, random.randint(0,225)/225, random.randint(0,225)/225)
    return rgb
rgb = []
#apply to amount of unique items
for i in range(len(df["Item"].unique())):
    rgb.append(rand_rgb())
#bar chart customization
plt.xlabel("items")
plt.ylabel("frequency")
plt.title("items to frequency", fontsize=10)
plt.xticks(fontsize=0.5)

#for each value(type=list) for each date (func param), find uniqueitems and itemcount to make a graph
def update(date):
    grocery = alldays.get(date)
    uniqueitems, itemcount = np.unique(grocery, return_counts=True) #x and y values
    sorting = itemcount.argsort() #sort according to itemcount (ascending)
    uniqueitems = uniqueitems[sorting]
    itemcount = itemcount[sorting]

    #show first 10 only
    head_uniqueitems = uniqueitems[-10:] #since both arrays are ascending, count backwards from highest index
    head_itemcount = itemcount[-10:]
    plt.barh(y=head_uniqueitems, height=0.5, width=head_itemcount, color=rgb)
    #text values
    for index, value in enumerate(head_itemcount):
        plt.text(value, index-0.1, str(value))
    plt.show()

testday = next(iter(alldays)) #first iteration of all days
update('2016-11-11')

#chart_animation = animation.FuncAnimation(fig, update, frames=alldays.keys(), repeat=False, interval=1000)