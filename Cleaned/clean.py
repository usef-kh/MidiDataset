import os
import pandas as pd
path = r'C:\Users\Yousef\Desktop\Uni\BU\MidiDataset\Cleaned\0 STILL NOT CLEANED I JUST COPIED THEM HERE SO I CAN EASILY MOVE STUFF AROUND\b\black_sabbath'
database_path = r'C:\Users\Yousef\Desktop\Uni\BU\MidiDataset\Cleaned\database.csv'
artist = 'Black Sabbath'
genre = 'Rock'

files = os.listdir(path)

for file in files:
    original = path + '\\' + file
    changed = path + '\\' + ' '.join(file.split('_'))
    os.rename(original, changed)

files = os.listdir(path)

song_names = []
for file in files:
    song_names.append(file.split('.mid')[0])

files = [[artist, song, genre] for song in song_names]

df = pd.DataFrame(files,columns = ['Artist', 'Song Name', 'Genre(s)'])

df.to_csv(database_path, index='False', header=False, mode='a')