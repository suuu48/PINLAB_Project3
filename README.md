![header](https://capsule-render.vercel.app/api?type=soft&color=006EDB&fontColor=DEEAF7&height=200&section=header&text=PINLAB&desc=Distribution%20WAV%20file%20recorder&descAlignY=80&fontSize=90)
# PINLAB_Project3
- Distribution WAV file recorder linked Cloud Database based on Docker

---

## Navigation
1. [Description](#Description)
2. [Getting started](#Getting-Started)
3. [Architecture](#Architecture)

---

## Description
Distribution WAV file recorder linked Cloud Database based on Docker on Jetson Nano board
- Recording(Saving) WAV file and Playing WAV file via Atlas(MongoDB)
    - [WAV file description](https://crystalcube.co.kr/123)
- Distribution via Docker

---

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
See deployment for notes on how to deploy the project on a live system.

### Installing & Setting (based on Code)
- Installing the pip
    - pip: for Python 2.x
    - pip3: for Python 3.x
```console
sudo apt-get install python-pip3
```

- Installing the [PyMongo](https://kb.objectrocket.com/mongo-db/how-to-install-pymongo-and-connect-to-mongodb-in-python-363)
```console
pip3 install pymongo
```

- More packate to install are in Dockerfile

### Installing & Setting (based on Docker)
- docker: [kimakuma8/ubuntu:project4](https://hub.docker.com/layers/kimakuma8/ubuntu/jetson/images/sha256-efc7f8b444cd68947ad227a118c639c337ffad62fd51a412190ee84dda8400f7?context=repo)

- Grant sound device permission in Docker
```console
sudo isermod -aG docker $USER
sudo su - $USER
docker run --device /dev/snd/ -it { Docker image }
```

---

## Architecture
### Docker
<img src="https://user-images.githubusercontent.com/76460405/204084157-f98f2178-5799-4da2-88bd-6eb2d32da4bf.png" width="590" height="214">

### Architecture
<img src="https://user-images.githubusercontent.com/76460405/204084264-f78f6e4c-fe85-4f4e-92ee-bdeac230467d.png" width="598" height="296">

---

## Stacks
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"> <img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=MongoDB&logoColor=white"> <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white">
