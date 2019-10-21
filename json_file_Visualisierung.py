
import json

import matplotlib.pyplot as plt


import matplotlib.pyplot as plt

with open("profile_data.json") as file:
    Data=json.load(file)

k=[]
v1,v2=[],[]

for i in range (len(Data)):
    for j in range (len(Data["Data1"])):
        if i==0:
            k.append(j+1)
            v1.append(float(Data["Data1"][str(j+1)][0]))
        else:
            v2.append(float(Data["Data2"][str(j+1)][0]))

#plt.scatter(v1,k)
print("Mohammed")
