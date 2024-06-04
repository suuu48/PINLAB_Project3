#!/usr/bin/env python3

## record
import argparse
import tempfile
import queue
import sys
import sounddevice as sd
import soundfile as sf
import numpy
assert numpy  # avoid "imported but unused" message (W0611)

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

def int_or_str(text):
    try:
        return int(text)
    except ValueError:
        return text

### Recording as a wav file ###
def record(filename):
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        '-l', '--list-devices', action='store_true',
        help='show list of audio devices and exit')

    args, remaining = parser.parse_known_args()

    if args.list_devices:
        print(sd.query_devices())
        parser.exit(0)

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[parser])

    parser.add_argument(
        'filename', nargs='?', metavar='FILENAME',
        help='audio file to store recording to')

    parser.add_argument(
        '-d', '--device', type=int_or_str,
        help='input device (numeric ID or substring)')

    parser.add_argument(
        '-r', '--samplerate', type=int, help='sampling rate')

    parser.add_argument(
        '-c', '--channels', type=int, default=1, help='number of input channels')

    parser.add_argument(
        '-t', '--subtype', type=str, help='sound file subtype (e.g. "PCM_24")')

    args = parser.parse_args(remaining)

    q = queue.Queue()

    def callback(indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        q.put(indata.copy())
                                
    try:
        device_info = sd.query_devices(args.device,'input')
        args.samplerate = int(device_info['default_samplerate'])

        with sf.SoundFile(filename, mode='x', samplerate=args.samplerate,
                        channels=args.channels, subtype=args.subtype) as file:
            with sd.InputStream(samplerate=args.samplerate, device=args.device,
                                channels=args.channels, callback=callback):

                print('( press Ctrl+C to stop the recording )')

                while True:
                    file.write(q.get())

    except KeyboardInterrupt:
        print('\nRecording finished: ' + repr(filename))
        print("")

    except Exception as e:
        parser.exit(type(e).__name__ + ': ' + str(e))

### Storing files in DB ###
def db_in(filename):
    cluster = MongoClient('localhost', 27017)
    db = cluster["buf1"]
    collection = db["buf1"]

    File = wavio.read(filename)
    wavio.write(filename, File.data, File.rate)

    collection.insert_one(
        {   "filename": filename,
            "rate": File.rate,
            "data": File.data.tolist(),
        })
    
    print("Successfully saving file to database")  
    print("")   
