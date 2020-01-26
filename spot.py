#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 14:17:51 2020

@author: Steffen
"""
import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
from flask import Flask, jsonify, request
from config import Config
from collections import OrderedDict
app = Flask(__name__)

# Flask_CORS
        
@app.route('/')
def spotify_test():
    
    with open('tracklist.txt') as trackid_file:
        top_tracks_ids = json.load(trackid_file)
        
    #print(top_tracks_ids)
    
    username = sys.argv[1]
    SCOPE = Config.CLIENT_SCOPE
    SPOTIPY_CLIENT_ID = Config.CLIENT_ID
    SPOTIPY_CLIENT_SECRET = Config.CLIENT_SECRET
    SPOTIPY_CLIENT_REDIRECT_URI = Config.REDIRECT_URI
    #os.getEnviron['CLIENT_ID']
    #export SPOTIPY_CLIENT_ID='28c97b38b4fb4668a1963fcbbd6d2353'
    #export SPOTIPY_CLIENT_SECRET='27554eea06cb4c4a832d01b87bf6b933'
    #export SPOTIPY_REDIRECT_URI='http://google.com/'
    
    #user_id = 	ahx2v4cknryduq19a58m1yx1b
        
    try:
        token = util.prompt_for_user_token(username, SCOPE, client_id = SPOTIPY_CLIENT_ID, client_secret = SPOTIPY_CLIENT_SECRET, redirect_uri = SPOTIPY_CLIENT_REDIRECT_URI)      
    
    except:
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username, SCOPE)
        
    sp = spotipy.Spotify(auth=token)
    
    
    top_tracks = sp.current_user_top_tracks(limit = 5, offset = 0, time_range = 'long_term')
    for i,track in enumerate(top_tracks['items']): 
        if track['id'] in top_tracks_ids:
            top_tracks_ids[track['id']] += 1
        else:
            top_tracks_ids[track['id']] = 1

        
    sorted_track_list = OrderedDict(sorted(top_tracks_ids.items(), reverse = True, key=lambda x: x[1]))
    
    with open('tracklist.txt', 'w') as outfile:
        json.dump(sorted_track_list,outfile, indent = 4,sort_keys = False)
    
    return sorted_track_list
    

#@app.route("/get_sorted/")
#def get_art(track_id:
 

    

# localhost:5000
if __name__ == "__main__":
   #app.run(host='0.0.0.0',debug=True)
   app.run(debug=True)