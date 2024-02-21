# Backend Challenge (API with Python)

## Natasha Serem

## Description
Create a simple Python Service, design a simple customers and orders database, implement authentication and authorization via OpenID Connect and when an order is added, send the customer an SMS alerting them then write unit tests (with coverage checking) and set up CI + automated CD.

### Setup and Installation
To get the code, clone the repository: And run the following commands;

- $ cd Voting-App 
- $ pip install -r requirements.txt

### Installing and activating Virtual Environment
- $ python3 -m venv virtual 
- $ source virtual/bin/activate

### Installing Django
- $ pip install django

### Installing Django rest Framework
Install the rest framework that will be used for REST API calls and endpoint creations;
- $ pip install djangorestframework

### Create a project
This is where you will carry out your project with all the necessary files;
- $ django-admin startproject [PROJECT_NAME]

### Running Migrations
Run migrations of your models file which is the table data for the database you have. To do so, run the following commands;
- $ python3 manage.py makemigrations [NAME_OF_APP]
- $ python3 manage.py migrate

### Create a Django Admin Dashboard
This dashboard will enable you to be able to have access rights to the entire site and make changes that can be easily seen and done. To have this dashboard, you need to create a super user with the following command;
- $ python3 manage.py createsuperuser
and provide a username and password for the super user.

