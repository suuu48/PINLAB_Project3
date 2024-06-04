FROM ubuntu:latest

RUN apt-get update
RUN apt-get install python3
# RUN wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | apt-get add -
RUN wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | apt-key add -
RUN echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list 
RUN apt-get update
RUN apt-get install -y mongodb-org # 안되는 경우 뒤에 org 빼고

RUN apt-get update
RUN apt-get upgrade

RUN apt-get install python3-pip

RUN apt-get update
RUN apt-get upgrade

RUN pip3 install pymongo

RUN apt-get update
RUN apt-get upgrade

RUN apt-get update
RUN apt-get upgrade

RUN pip3 install numpy
RUN pip3 install requests
RUN pip3 install read
RUN pip3 install write
RUN pip3 install wavfile
RUN pip3 install sounddevice
RUN pip3 install wavio
RUN pip3 install pyglet
RUN pip3 install argparse
RUN pip3 install soundfile
RUN pip3 install playsound

RUN apt-get update
RUN apt-get upgrade

RUN apt install libasound-dev
RUN apt install alsa

RUN apt install libsndfile1
RUN apt install python3-scipy

## file copy & portaudio setup

# kimakuma8/ubuntu:wav
