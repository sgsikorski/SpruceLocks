import tkinter as tk
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import time

SCOPE = "user-modify-playback-state"
user = True
redirect_uri = "http://localhost:8080"
client_id = ''
client_secret = ''
tracks = ['', '', '', '', '', '', '', '', '', '']
songUris = ['', '', '', '', '', '', '', '', '', '']

def exit(event):
    root.destroy()

def onDownstairs(fr, fr2):
    user = True
    fr.pack_forget()
    fr2.pack()
    return

def onUpstairs(fr, fr2):
    user = False
    fr.pack_forget()
    fr2.pack()
    return

def submitRequest(fr2, fr3, lFrame, song):
    handleRequest(song, fr3)
    fr2.pack_forget()
    fr3.pack()
    return

def handleRequest(songTit, fr3):
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    queryRes = sp.search(songTit, limit=10, type="track")
    num=0
    for searches in ((queryRes.get('tracks')).get('items')):
        artists = ''
        for arts in searches.get('artists'):
            artists += arts.get('name') + ', '
        tracks[num] = artists
        songUris[num] = searches.get('uri')
        num+=1
    num = 0
    for child in fr3.children.values():
        if isinstance(child, tk.Label): continue
        child['text'] = tracks[num]
        num+=1
    return

def addToQ(pos, fr3, fr, lFrame):
    fr3.pack_forget()
    auth_manager = SpotifyOAuth(scope=SCOPE, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    sp.add_to_queue(songUris[pos])
    fr.pack()
    return 

root = tk.Tk()
root.geometry("1024x600")
# root.attributes('-fullscreen', True)
root.bind('<Escape>', exit)
tk.Label(text="Request Songs", font=('Georgia 24')).pack()
tk.Label(text="Please be patient. If you pressed the button, it worked", font=('Georgia 24')).pack()

fr = tk.Frame(root, highlightbackground='black', highlightthickness=5)
fr2 = tk.Frame(root, highlightbackground='black', highlightthickness=5)
lFrame = tk.Frame(root, highlightbackground='black', highlightthickness=5)
fr3 = tk.Frame(root, highlightbackground='black', highlightthickness=5)
usBut = tk.Button(fr, text="Upstairs", height = 10, width = 100, command=lambda: onUpstairs(fr, fr2), font=('Georgia 20'))
# dsBut = tk.Button(fr, text="Downstairs", height = 10, width = 100, command=lambda: onDownstairs(fr, fr2), font=('Georgia 20')).pack()
usBut.pack()
fr.pack()

query = tk.Entry(fr2, text="Enter the song title", font=('Georgia 48'))
query.pack()
submitBut = tk.Button(fr2, text="Submit", command=lambda: submitRequest(fr2, fr3, lFrame, query.get()), font=('Georgia 20')).pack()
fr2.pack()
fr2.pack_forget()

tk.Label(lFrame, text='Loading. Fucking wait.', font=('Georgia 48')).pack()
lFrame.pack()
lFrame.pack_forget()

tk.Label(fr3, text='Pick by which artists', font=('Georgia 40')).pack()
s1 = tk.Button(fr3, text=tracks[0], command=lambda: addToQ(0, fr3, fr, lFrame)).pack()
s2 = tk.Button(fr3, text=tracks[1], command=lambda: addToQ(1, fr3, fr, lFrame)).pack()
# s3 = tk.Button(fr3, text=tracks[2], command=lambda: addToQ(2, fr3, fr)).pack()
# s4 = tk.Button(fr3, text=tracks[3], command=lambda: addToQ(3, fr3, fr)).pack()
# s5 = tk.Button(fr3, text=tracks[4], command=lambda: addToQ(4, fr3, fr)).pack()
# s6 = tk.Button(fr3, text=tracks[5], command=lambda: addToQ(5, fr3, fr)).pack()
# s7 = tk.Button(fr3, text=tracks[6], command=lambda: addToQ(6, fr3, fr)).pack()
# s8 = tk.Button(fr3, text=tracks[7], command=lambda: addToQ(7, fr3, fr)).pack()
# s9 = tk.Button(fr3, text=tracks[8], command=lambda: addToQ(8, fr3, fr)).pack()
# s10 = tk.Button(fr3, text=tracks[9], command=lambda: addToQ(9, fr3, fr)).pack()
fr3.pack()
fr3.pack_forget()

root.mainloop()
