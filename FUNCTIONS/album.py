def make_album(artist_name,title,songs = None):
    album = {'Name: ':artist_name, 'Album:':title}
    
    if songs:
        album['Songs: ']=songs

    return album


while True:

    artist = input("Artist: ")
    
    if artist=='-1':
            break

    album = input("Album: ")
    songs = input("Songs: ")

    if int(songs)>0:
        print(make_album(artist,album,songs))
    else:
        print(make_album(artist,album))


    
