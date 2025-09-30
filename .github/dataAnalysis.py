import pandas as pd
import random

names = []
f_names = []
l_names = []

for i in range(30):
    names.append(f"{random.choice(f_names)} {random.choice(l_names)}")
    
data = {
    "Name": names,
    "Grade": [random.randint(9,12) for _ in names],
    "Hrs Spent Reading": [random.randint(0,60) for _ in names],
    "Enjoy English Class":,
    "Enjoy Reading ":,
    "Enjoy Writing":,
}

pennData = pd.DataFrame(data)
print(pennData)

pennData.to_csv("pennData.csv", index=False)