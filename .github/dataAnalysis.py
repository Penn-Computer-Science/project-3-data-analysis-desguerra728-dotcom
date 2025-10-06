import pandas as pd
import random
import matplotlib.pyplot as plt

f_names = ['N', 'A', 'K', 'V', 'A', 'K', 'B', 'R']
l_names = ['Bradberry', 'Luebke', 'Kedrychowicz', 'Latson', 'Girton', 'Fogarty', 'Martin', 'Williams']
p_grades = [9, 10, 11, 12]
names = []
p_hours = ['<1', '2', '3', '3+']

grades = [10,11,10,11,11,10,12,12]
hours = ['<1', '3+', '2', '<1', '<1', '3', '<1', '1']
lang = [2,2,1,4,3,3,2,2]
read = [3,5,2,2,0,2,3,1]
write = [2,5,1,5,1,4,1,4]

for i in range(8):
    names.append(f"{f_names[i]}. {l_names[i]}")

for i in range(22):
    names.append(f"{random.choice(f_names)}. {random.choice(l_names)}")
    grades.append(random.choice(p_grades))
    hours.append(random.choice(p_hours))
    lang.append(random.randint(0,5))
    read.append(random.randint(0,5))
    write.append(random.randint(0,5))

data = {
 'Name': names,
 'Grade': grades,
 'Hrs reading per week': hours,
 'Lang.Arts Class': lang,
 'Reading': read,
 'Writing': write,
}

data = pd.DataFrame(data)
print(data)
print(data.describe())
print(data.info())

data.to_csv("data.csv", index = False)

print(data.groupby('Reading')['Writing'])
data.groupby('Reading')['Writing'].mean().plot(kind="bar")
plt.title("Average Writign by Reading")
plt.xlabel("Reading")
plt.ylabel("Writing")
plt.show()