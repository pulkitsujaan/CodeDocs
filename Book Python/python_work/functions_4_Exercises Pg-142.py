# # Exercise 8-6
# def city_country(city,country):
#     full=f'{city}, {country}'
#     print(full.title())
# city_country(city='meerut',country='india')
# city_country(city='mumbai',country='india')
# city_country(city='tokyo',country='japan')

# # Exercise 8-7
# def music_album(artist,album_title,no_of_songs=None):
#     album={
#         'Artist':artist,
#         'Album Title':album_title
#     }
#     if no_of_songs:
#         album['No. of Songs']=no_of_songs
#     return album
# m_album=music_album(artist='Billie Eilish',album_title='Happier Than Ever')
# print(m_album)

# Exercise 8-8
def music_album(artist,album_title,no_of_songs=None):
    album={
        'Artist':artist,
        'Album Title':album_title
    }
    if no_of_songs:
        album['No. of Songs']=no_of_songs
    return album
while True:
    print("Enter 'q' to quit")
    Artist=input('Enter the name of the Artist: ')
    if Artist=='q':
        break
    AlbumTitle=input("Enter album Title: ")
    if AlbumTitle=='q':
        break
    Songs=int(input('How many songs are there in the album(in number): '))
    if Songs=='q':
        break
    Album=music_album(artist=Artist, album_title=AlbumTitle,no_of_songs=Songs)
    print(f'\n{Album}\n')