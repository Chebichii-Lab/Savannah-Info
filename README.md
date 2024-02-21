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
The dashboard can be accessed via the url;
- http://127.0.0.1:8000/admin/
username: admin
password: admin123

### Performing CRUD operations
This is to perform the Create, Read, Update and Delete operations for the API client. The following are the url links for various CRUD operations for the Customer and Orders;
1. GET
- http://127.0.0.1:8000/customers/ (get all customers in the database)
- http://127.0.0.1:8000/orders/ (get all orders in the database)

2. POST
- http://127.0.0.1:8000/customers/ (add a new customer to the database via the API endpoint)
- http://127.0.0.1:8000/orders/ (add a new customer to the database via the API endpoint)
Whatever you add via the API will also reflect on the Django Admin Dashboard and vice versa.

3. PUT
- http://127.0.0.1:8000/customers/3 (update the customer with ID number 3 to show that you can update a customer of choice)
- http://127.0.0.1:8000/orders/2 (update the order with ID number 2 to show that you can update an order of choice)
This updates can be see via browser when you visit the links and also via the Django admin dashboard.

### Implement authentication and authorization via OpenID Connect
OpenID Connect is a package that is used to monitor authentication and authorization to your APIs.
1. Install OpenID Connect using the following command;
- $ pip install django-oidc-provider
2. Add it to your INSTALLED APPS section in the settings.py file;
    - INSTALLED_APPS = [
    # ...
    'oidc_provider',
    # ...
]
3. Include it in your ursl.py file
    urlpatterns = [
    # ...
    path('openid/', include('oidc_provider.urls', namespace='oidc_provider')),
    # ...
]
4. Run migrations and generate and RSA key
    - $ python manage.py migrate
    - $ python manage.py creatersakey

5. Set up the client side in your Django Admin Dashboard.

### 

