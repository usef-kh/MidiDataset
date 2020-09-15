import pandas as pd

database_path = r'.\database.csv'
database = pd.read_csv(database_path, encoding = "ISO-8859-1")

with open("song_names.txt", "w") as output:
    for index, row in database.iterrows():
        song = row['Song Name'] + ' - ' + row['Artist']
        output.write(song + '\n')






