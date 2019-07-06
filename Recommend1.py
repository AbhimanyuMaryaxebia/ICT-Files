import pandas as pd
import numpy as np
import time
from tkinter import *
from sklearn.model_selection import train_test_split


def Instrumental():
    triplets_file = 'D:\Instrumental.txt'
    # songs_metadata_file = 'D:/song_data (1).csv'
    songs_metadata_file = 'D:\Instrumental.csv'
    songs_df_2 = pd.read_csv(songs_metadata_file);
    train_data, test_data = train_test_split(songs_df_2, test_size=0.20, random_state=0)
    print(test_data.head(5))


def Yoga():
    triplets_file = 'D:\Instrumental.txt'
    songs_metadata_file = 'D:/song_data (1).csv'

    songs_df_1 = pd.read_table(triplets_file);
    songs_df_2 = pd.read_csv(songs_metadata_file);

    songs_df_1.columns = ['user_id', 'song_id', 'listen_count']
    songs = pd.merge(songs_df_1, songs_df_2.drop_duplicates('song_id'), on="song_id", how="left")
    songs['song'] = songs['title'].map(str) + " - " + songs['artist_name']

    song_grouped = songs.groupby(['song']).agg({'listen_count': 'count'}).reset_index()
    grouped_sum = song_grouped['listen_count'].sum()
    song_grouped['percentage'] = song_grouped['listen_count'].div(grouped_sum) * 100
    song_grouped.sort_values(['listen_count', 'song'], ascending=[0, 1])
    train_data, test_data = train_test_split(songs, test_size=0.20, random_state=0)
    print(train_data.head(5))



def Aerobics():
    songs_metadata_file = 'D:\Aerobics.csv'
    songs_df_2 = pd.read_csv(songs_metadata_file);
    train_data, test_data = train_test_split(songs_df_2, test_size=0.20, random_state=0)
    print(test_data.head(5))




root = Tk()
canvas = Canvas(root, width=250, height=250)
canvas.pack()
photo = PhotoImage(file="D:\images.png")
canvas.create_image(125, 125, image=photo)
button1= Button(root,text="Instrumental ",command=Instrumental, fg='Red',anchor='w')
window1 = canvas.create_window(25, 45, anchor='nw', window=button1)
button2= Button(root,text="Yoga",command=Yoga,fg='Blue')
window2 = canvas.create_window(25, 75, anchor='nw', window=button2)
button3= Button(root,text="Aerobics",command=Aerobics,fg='Green')
window3 = canvas.create_window(25, 105, anchor='nw', window=button3)
root.mainloop()

