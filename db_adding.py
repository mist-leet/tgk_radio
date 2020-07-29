import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tgk_radio.settings")
django.setup()

from radio_main.models import Song
import sys
from os import listdir
import eyed3


def run():
    #url = ''
    #for i in range(1, len(sys.argv)):
    #    url += sys.argv[i] + " "
    #url = url.replace('\\', '/')[:-1]
    #print(url)
    url = input()
    files = listdir(url)
    songs = filter(lambda x: x.endswith('.mp3'), files)
    files = []
    for song in songs:
        song_tag = eyed3.load(url + '/' + song)
        files.append(song_tag.tag.artist + ' - ' + song_tag.tag.title)
    for file in files:
        print((file + ' added'))
        new_song = Song(name=file)
        new_song.save()

run()
