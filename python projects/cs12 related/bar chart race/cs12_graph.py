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

uniqueitems = df["Item"].unique() #x-axis values
itemcount = list(df.value_counts()) #y-axis values

#gen random rgb (hex code doesn't work??????)
def rand_rgb():
    rgb = (random.randint(0,225)/225, random.randint(0,225)/225, random.randint(0,225)/225)
    return rgb

rgb = []
#apply to amount of unique items
for i in range(len(uniqueitems)):
    rgb.append(rand_rgb())

#bar chart customization
plt.xlabel("items")
plt.ylabel("frequency")
plt.title("items to frequency (total)", fontsize=10)
plt.xticks(fontsize=5.8, rotation=85)

plt.bar(x=uniqueitems, height=itemcount, width=0.5, color=rgb) #i'll stick with vertical bars
plt.show()