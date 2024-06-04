#!/usr/bin/env python3

## database
from io import BytesIO
import numpy as np 
import requests
from pymongo import MongoClient
from scipy.io.wavfile import read, write
from scipy.io import wavfile
import sounddevice as sd
import wavio
import pyglet

## play
from playsound import playsound

### Finding files in DB ###
def db_out(filename_p):
    cluster = MongoClient('localhost', 27017)
    db = cluster["buf1"]
    collection = db["buf1"]

    # query for find data
    results = collection.find({"filename":filename_p})

    # db data -> wav file
    for result in results:
        wavio.write(filename_p, np.array(result["data"], dtype = np.int32), result["rate"])

### Playing wav file ###  
def play(filename_p):
    playsound(filename_p)
