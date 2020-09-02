import os
import pandas as pd
genre = 'Rock'
database_path = r'C:\Users\Yousef\Desktop\Uni\BU\MidiDataset\Cleaned\database.csv'
folders = os.walk(r'C:\Users\Yousef\Desktop\Uni\BU\MidiDataset\Cleaned\zzzzz')

for folder in folders:
    path, _, files = folder
    if files and files[0][-4:] == '.mid':

        sections = path.split('\\')
        artist = sections[-1]
        artist = ' '.join(artist.split('_'))


        song_names = []
        for file in files:
            original = path + '\\' + file

            song_name = ' '.join(file.split('_'))
            changed = path + '\\' + song_name

            song_names.append(song_name[:-4])   # remove '.mid'

            os.rename(original, changed)

        files = [[artist, song, genre] for song in song_names]

        df = pd.DataFrame(files, columns = ['Artist', 'Song Name', 'Genre(s)'])

        df.to_csv(database_path, index='False', header=False, mode='a')