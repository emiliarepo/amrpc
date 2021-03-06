from pypresence import Presence
import time
import math

class Discord:
    def __init__(self, id):
        self.id = id
        self.rpc = Presence(id)
        self.cleared = True
        self.rpc.connect()

    def clear(self):
        if self.cleared == False:
            print("Clearing status")
            self.rpc.clear()

        self.cleared = True

    def setTrack(self, track):

        # thanks stack over flow ,
        trackName = track.track.encode().decode("unicode-escape").encode("ISO-8859-1").decode("utf8")
        artistName = track.artist.encode().decode("unicode-escape").encode("ISO-8859-1").decode("utf8")
        print("Changing track to: " + trackName + " by " + artistName + "(" + artistName.lower().replace(' ', '_') + ")")
        self.cleared = False
        self.rpc.update(
            state="by " + artistName,
            details=trackName + "  ", # discord wants at least 2 characters - add invisible chars!
            start=time.time()-math.ceil(track.position),
            large_image="logo",
            large_text="Apple Music")
            #small_image="logo",
            #small_text="github.com/leahlundqvist")