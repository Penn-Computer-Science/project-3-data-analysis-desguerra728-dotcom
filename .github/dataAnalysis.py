import pandas as pd
import random

f_names = ['Noah', 'Alexis', 'Katerina', 'Van', 'Aiden', 'Kyan', 'Ben', 'Martin', 'Roman']
l_names = ['Bradberry', 'Luebke', 'Kedrychowicz', 'Latson', 'Girton', 'Fogarty', 'Martin', 'Williams']
grades = [10, 11, 12]
names = []
hours = ['<1', '2', '3', '3+']

for i in range(30):
    names.append(f"{random.choice(f_names)} {random.choice(l_names)}")

junk_data = {
 'Name': names,
 'Grade': [random.choice(grades) for _ in names],
 'Hrs reading per week': [random.choice(hours) for _ in names],
 'Lang.Arts Class': [random.randint(0,5) for _ in names],
 'Reading': [random.randint(0,5) for _ in names],
 'Writing': [random.randint(0,5) for _ in names],
}

data = pd.DataFrame(junk_data)
print(data)
print(data.describe())


data.to_csv("data.csv", index = False)