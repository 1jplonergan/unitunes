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
