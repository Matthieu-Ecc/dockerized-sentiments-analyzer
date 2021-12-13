# Data Engineering II Project
Mise en production d'un modele d'analyse de sentiments.

### Team Members
- Sahnou Numan
- Eccher Matthieu
- Edjekouane Rayan

## Project Summary

As a part of the curriculum of the Master 2 (M2) course entitled &quot;Data Engineering II&quot;, the students will complete a team project work. The purpose of this project is to combine all the skills collected throughout the course thus far, and to provide a solid example of real-life application development in a DevOps environment.

The following sections provide necessary information about the description of the application to be created.

Instructor: **Khodor Hammoud**.

## Goals :

- The application is a sentiment analysis application, which, given a piece of text, should be able to reply with its sentiment as being positive, negative, or neutral.
- The text language used must be English
- The application should have a web interface with an input form and a submit button, where users can input their sentences, and hit submit, and the sentiment of their sentence will be presented.
- The accuracy of the sentiment analyzer should be above 80%
- The application must be easily deployable

## Project architecture :

- __dockerized-sentiments-analyzer : this is the root directory of the project__
  - `docker-ml : folder containing the actual sentiment analyzer script with a function which, given a piece of text, replies with its sentiment`
    - analyzer.py : actual sentiment analyzer script
    - vader_API.py : Flask REST Api application that runs the sentiment analyzer script and return the sentiment throught a GET request
    - requirements.txt : dependencies
    - Dockerfile : Dockerfile to build & run the image
  - `docker_web  : contains the flask web application`
    - app.py : Flask application (the base route display the form & the /data call the Vader Api with the piece of text 
    - routes.py : definition of the different routes of the Flask Application 
    - requirements.txt : dependencies
    - Dockerfile : Dockerfile to build & run the image
    - templates : folder containing the index.html file
  - `docker-compose.yaml : requirements of the docker-compose`
  - `test_app.py : test of the model & the web service`


### 2 microservices :
- Interface Web
- Conteneur d'inference du modele

## How to set up the project :

- Git clone the project into a directory using the following command : `git@github.com:Matthieu-Ecc/dockerized-sentiments-analyzer.git`

- Install docker

- ``docker-compose up`` in the folder to test the website

- To launch the tests, you have to pip install :

  - flask
  - nltk
  - flask_restful
  - vaderSentiment
  - numpy
  - beautifulsoup4
