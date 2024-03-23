# references used for this code
# https://pypi.org/project/kmodes/
# https://anaconda.org/conda-forge/kmodes

import pandas as pd
from kmodes.kmodes import KModes

# Load the dataset
data_path = './data.xlsx'
data = pd.read_excel(data_path)

# Dropping the first column (non numerical)
clustering_data = data.drop(data.columns[0], axis=1)

# Initialize and fit the K-Modes algorithm
km = KModes(n_clusters=4, init='Huang', n_init=5, verbose=1, random_state=0)
clusters = km.fit_predict(clustering_data)

# Add clusters to the file
data['Cluster'] = clusters

# Group by cluster and calculate counts
clustered_data = data.groupby('Cluster').size()

# Display the size of each cluster
print(clustered_data)

# sorting the data
data = data.sort_values(by='Cluster')

# writing xlsx file
output_file = 'clustered_data_kmodes.xlsx'
data.to_excel(output_file)
