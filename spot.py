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
from flask import Flask

app = Flask(__name__)

@app.route('/')
def spotify_test():
    username = sys.argv[1]
     
    #export SPOTIPY_CLIENT_ID='28c97b38b4fb4668a1963fcbbd6d2353'
    #export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
    #export SPOTIPY_REDIRECT_URI='http://google.com/'
    
    #user_id = 	ahx2v4cknryduq19a58m1yx1b
        
    try:
        token = util.prompt_for_user_token(username)
    
    except:
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username)
        
    spotifyObject = spotipy.Spotify(auth=token)
        
    user = spotifyObject.current_user()
    return (json.dumps(user, sort_keys = True,indent = 4))



if __name__ == "__main__":
   app.run(debug=True)