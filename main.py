#!/usr/bin/env python3

import record
import play

import os

### main ###
while True:
    os.system("clear")

    print("<< menu >>")
    print("1. record")
    print("2. play")
    print("")

    menu = input("menu >> ")
    print("")

    if menu == '1':
        os.system("clear")
        print("<< record >>")
        print("")
        filename = input("filename( .wav) : ")
        print("")

        record.record(filename)
        record.db_in(filename)

        print("finish...")
        input("go to back?")

    elif menu == '2':
        os.system("clear")
        print("<< play >>")
        print("")
        filename_p = input("filename : ")

        play.db_out(filename_p)
        play.play(filename_p)

        print("")
        print("finish...")
        input("go to back?")

    else:
        print("bye...")
        exit(1)
