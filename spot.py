m#!/usr/bin/env python3
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
        
@app.route('/<username>')
def spotify_test(username):
    
    username = 'sdreesen16'
    
    with open('tracklist.txt') as trackid_file:
        top_tracks_ids = json.load(trackid_file)
    
    #username = sys.argv[1]
    SCOPE = Config.CLIENT_SCOPE
    SPOTIPY_CLIENT_ID = Config.CLIENT_ID
    SPOTIPY_CLIENT_SECRET = Config.CLIENT_SECRET
    SPOTIPY_CLIENT_REDIRECT_URI = Config.REDIRECT_URI

    #user_id = 	ahx2v4cknryduq19a58m1yx1b
        
    token = util.prompt_for_user_token(username, SCOPE, client_id = SPOTIPY_CLIENT_ID, client_secret = SPOTIPY_CLIENT_SECRET, redirect_uri = SPOTIPY_CLIENT_REDIRECT_URI)      
    
    if token: 
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        
yp        top_tracks = sp.current_user_top_tracks(time_range = 'long_term', limit = 3)

        
        for i,track in enumerate(top_tracks['items']): 
            if track['name'] in top_tracks_ids:
                top_tracks_ids[track['name']] += 1
            else:
                top_tracks_ids[track['name']] = 1
                
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