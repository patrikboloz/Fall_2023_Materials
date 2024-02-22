"""Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Use None to add an optional parameter to make_album() that allows you to
store the number of songs on an album. If the calling line includes a value for
the number of songs, add that value to the album’s dictionary. Make at least
one new function call that includes the number of songs on an album."""

def make_album(artist, title, songs=None):
    album = {
        'artist': artist,
        'title': title
    }
    if songs is not None:
        album['songs'] = songs
    return album

album1 = make_album("T-Pain", "Epiphany", 14)
album2 = make_album("Linkin Park", "Living Things")
album3 = make_album("Sabaton", "The Great War", 12) 

print(album1)
print(album2)
print(album3)
