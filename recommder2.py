# import pandas
# import numpy as np
# from sklearn.model_selection import train_test_split
#
# desired_width = 320
# pandas.set_option('display.width', desired_width)
# songs_metadata_file = 'D:\song_data (1).csv';
# triplets_file = 'https://static.turi.com/datasets/millionsong/10000.txt';
# song_df_1 = pandas.read_table(triplets_file,header=None)
# song_df_1.columns = ['user_id', 'song_id', 'listen_count']
#
# song_df_2= pandas.read_csv(songs_metadata_file)
# song_df =pandas.merge(song_df_1,song_df_2.drop_duplicates(['song_id']),on="song_id",how="left")
#
# song_df=song_df.head(10000);
# song_df['song']=song_df['title'].map(str)+" - "+ song_df['artist_name']
# song_df_grouped= song_df.groupby(['song']).agg({'listen_count':'count'}).reset_index()
# song_df_grouped.sort_values('listen_count',ascending=False,inplace=True)
# train_data,test_data= train_test_split(song_df,test_size=0.20,random_state=0)
#
# print(train_data.head(5))
#
