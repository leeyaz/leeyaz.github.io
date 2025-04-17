# Import your code from the previous exercise
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ogdf = pd.read_csv(r"BreadBasket_DMS_shortened.csv")

#Get rid of unused data
drop_time_and_trans = ogdf.drop(["Time", "Transaction"], axis=1)

#Date as what animates the data (the index/x-axis)
df = drop_time_and_trans.set_index("Date")

uniqueitems = df["Item"].unique()[::-1] #x-axis values
itemcount = list(df.value_counts())[::-1] #y-axis values

#gen random rgb (hex code doesn't work??????)
def rand_rgb():
    rgb = (random.randint(0,225)/225, random.randint(0,225)/225, random.randint(0,225)/225)
    return rgb
rgb = []
#apply to amount of unique items
for i in range(len(uniqueitems)):
    rgb.append(rand_rgb())
print(rgb)

#bar chart customization
plt.xlabel("items")
plt.ylabel("frequency")
plt.title("items to frequency (total)", fontsize=10)
plt.xticks(fontsize=0.5)

#show first 10 only
head_uniqueitems = uniqueitems[-10:]
head_itemcount = itemcount[-10:]

plt.barh(y=head_uniqueitems, height=0.5, width=head_itemcount, color=rgb)
#text values
for index, value in enumerate(head_itemcount):
    plt.text(value, index-0.1, str(value))

plt.show()