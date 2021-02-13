#!/usr/bin/env python3
from music import getPlaying, Track
from discord import Discord
import time

playing = Track(0,0,0,0,0)
client = Discord("635251785136603166")
global previous
previous = 0

def update(current):
    track = getPlaying()

    global previous
    if track == False:
        previous = 0
        client.clear()
        return current
    
    # quick and dirty way to detect if position has changed
    # idk i havent used python in years
    diff = abs(previous - track.position)
    previous = track.position

    if current.equals(track) == False or diff > 5:
        client.setTrack(track)
        return track

    return current

while True:
    playing = update(playing)
    time.sleep(1)