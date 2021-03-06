# NM Trip
This project is called "NM Trip" and the aim is to practice using what I've learned so far in my journey to become a developer - HTML (including responsive images with the help of GraphicsMagick and Grunt), CSS (using Sass and Simple Grid), and Python (using Flask). It is Dockerized and deployed with Amazon Fargate at https://spk.sandytravelsnewmexico.com. Static resources are served via Amazon S3 buckets. 

# Getting Started

To grab code:
- Navigate to this repo: sandykaur2008/NM-Trip
- Follow these instructions: https://help.github.com/articles/cloning-a-repository/

# Prerequisites
Aside from a working browser and Python 3, you will also need:

- the dependencies in requirements.txt 

## To install dependencies in requirements.txt

Make sure you're in root directory of repo and execute:

```pip install -r requirements.txt```

## To actually run website once repo cloned, css compiled, and dependencies installed

- Navigate to root directory
- Execute: 

```export FLASK_APP=nmtrip.py```

```flask run```

- Navigate to link provided 

# Built With
- Visual Studio Code 1.23.1
- Ruby Sass 3.5.6 
- Flask 1.0.2 (see requirements.txt for extensions used). 
- Grunt 0.4.5 

# Authors
Satinder Kaur 

# License
Images are mine

# Acknowledgments
Thanks, @markalexandercastillo, for reviewing and giving me tips

Also, relied heavily on https://blog.miguelgrinberg.com/. 
