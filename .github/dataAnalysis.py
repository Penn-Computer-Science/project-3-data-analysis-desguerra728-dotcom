import pandas as pd
import random

f_names = ['Noah', 'Alexis', 'Katerine', 'Van', 'Aiden']
l_names = ['Bradberry', 'Luebke', 'Kedrychowicz', 'Latson', 'Girton']
grades = [10, 11]
names = []
hours = ['<=1', '2', '3', '3+']


for i in range(30):
    names.append(f"{random.choice(f_names)} {random.choice(l_names)}")



junk_data = {
 'Name': names,
 'Grade': [random.choice(grades) for _ in names],
 'Hrs reading per week': [random.choice(hours) for _ in names],
 'Language Arts Class': [],
 'Reading': [],
 'Writing': [],
}

data = pd.DataFrame(junk_data)
print(data)

data.to_csv("data.csv", index = False)