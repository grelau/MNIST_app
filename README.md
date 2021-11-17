## Flask application for hand written digit recognition using CNN
## Requirements
You will need git and docker desktop installed
## Installation
Open a command prompt to git clone this repo
```bash
git clone https://github.com/LGrAr/MNIST_app.git lgrar_mnist_app
```
change directory to the cloned repo
```bash
cd lgrar_mnist_app
```
build the docker image
```bash
docker build -t mnist_app .
```
run the docker image
```
docker run -d -p 80:80 mnist_app
```
click <a href="http://127.0.0.1" target="_blank">http://127.0.0.1</a> to open a web browser and access the app
