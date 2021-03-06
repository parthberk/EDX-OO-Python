class Artist:
    def __init__(self, name, label):
        self.name = name
        self.label = label

class Song:
    def __init__(self, name, album, year, artist):
        self.name = name
        self.album = album
        self.year = year
        self.artist = artist
        
def get_song_string(song):
    name=str(song.name)
    arts=str(song.artist.name)
    year=str(song.year)
    actual_string= "\"" + name + "\"" + " - " + arts + " " + "(" + year + ")"
    return actual_string
        
#The code below will test your function. It isn't used for
#grading, so feel free to modify it.
newArtist = Artist("Taylor Swift", "Big Machine Records, LLC")
newSong = Song("You Belong With Me", "Fearless", 2008, newArtist)
print(get_song_string(newSong))