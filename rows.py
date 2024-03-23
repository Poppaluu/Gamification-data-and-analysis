import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = 'data.xlsx'

df = pd.read_excel(file_path)

# Names of the shopping apps in the order they appear in the rows
shopping_apps = [
    'Temu: Shop like a billionaire', 'Vinted', 'Klarna | Shop now. Pay later', 
    'SHEIN-Shopping Online', 'Zalando - online fashion store', 'IKEA', 'Lindex', 
    'Tori.fi', 'alibaba.com', 'shop', 'cityshoppari', 'amazon shopping', 
    'booztlet', 'boozt', 'HobbyHall.fi', 'Pandabuy', 'Zaful', 'Zadaa', 'LighInTheBox'
]

counts = []

# counting the amount of gamification in each application
for index, row in df.iterrows():
    count = np.sum(row == 1)
    counts.append(count)

# changing size
width = 0.5
fig, ax = plt.subplots(figsize=(12, 6))

# visual tweaks
ax.bar(shopping_apps, counts, width)
ax.set_title('Amount of Gamification in Shopping Applications')
plt.xticks(rotation=45, ha='right', fontsize=8)
plt.ylim(0, 20)
plt.yticks(np.arange(0, 20, 1))
plt.subplots_adjust(bottom=0.3)

plt.show()
