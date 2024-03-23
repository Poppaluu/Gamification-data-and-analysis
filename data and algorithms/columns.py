import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = 'data.xlsx'

df = pd.read_excel(file_path)

# names of the gamification elements in the order they appear in the columns
gamification_elements = [
    'Acknowledgement', 'Chance', 'Competition', 'Cooperation', 'Economy', 'Imposed Choice',
    'Level', 'Narrative', 'Novelty', 'Objectives', 'Point', 'Progression', 'Puzzles', 'Rarity',
    'Renovation', 'Reputation', 'Sensation', 'Social Pressure', 'Stats', 'Storytelling', 'Time pressure'
]

counts = []

iter_columns = iter(df.items())
next(iter_columns)

# counting the amount of each gamification element found in the applications
for column_name, column_data in iter_columns:
    count = np.sum(column_data == 1)
    counts.append(count)

# changing size
width = 0.5
fig, ax = plt.subplots(figsize=(12, 6))  # Adjust the figure size

# visual tweaks
ax.bar(gamification_elements, counts, width)
ax.set_title("Amount of gamification in shopping applications")
plt.xticks(rotation=45, ha='right', fontsize=8)
plt.ylim(0, 20)
plt.yticks(np.arange(0, 20, 1))
plt.subplots_adjust(bottom=0.2)

plt.show()
