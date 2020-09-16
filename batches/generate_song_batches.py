import pandas as pd
import numpy as np

database_path = r'..\Cleaned\database.csv'
database = pd.read_csv(database_path, encoding="ISO-8859-1")

songs = []
for index, row in database.iterrows():
    songs += [row['Song Name'] + ' - ' + row['Artist']]

batch_size = 70
n_batches = ((len(database) - 1) // batch_size) + 1
batches = np.array_split(np.array(songs), n_batches)
# print(len(batches))
for i, batch in enumerate(batches):
    filename = 'batch_' + str(i) +'.txt'
    with open(filename, 'w') as output:
        for song in batch:
            output.write(song + '\n')

