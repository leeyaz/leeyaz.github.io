
dict = {}
for i in range(1,5):
    dict["lo"+ str(i)] = []
print(dict)

for index, key in enumerate(dict):
    dict[key].append(index)
print(dict)