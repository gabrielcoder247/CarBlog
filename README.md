## ExcellaCar Blog, is a web blog for subscribers to get latest information on cars and it accessory created 
### september, 17TH,  2018
#### By **[GABRIEL NWACHUKWU](https://github.com/gabrielcoder247)**

## Description
    ExcellaCar Blog, is a web blog meant for users to subscribe then get subscriptional mails on new update


A user can register  and get subscription for emails for latest news and upate

A user can select any of the categories from the dropdown navbar to view the pitches on these categories

Other users can give feedback to the pitch posts by commenting, liking or disliking the pitch. 


## Specifications
Get the specs [here](https://github.com/gabrielcoder247/https://github.com/gabrielcoder247/CarBlog/blob/master/SPECS.md)

## Set-up and Installation

### Prerequiites
    - Python 3.6
    - Ubuntu software

### Clone the Repo
Run the following command on the terminal:
`git clone https://github.com/gabrielcoder247/CarBlog && cd PitchIt on your machine terminal`

Install [Postgres](https://www.postgresql.org/download/)

### Create a Virtual Environment
Run the following commands in the same terminal:
`sudo apt-get install python3.6-venv`
`python3.6 -m venv virtual`
`source virtual/bin/activate, to activate the virtual environment`

### Install dependancies
Install dependancies that will create an environment for the app to run
`pip3 install -r requirements`

### Prepare environment variables
```bash
export DATABASE_URL='postgresql+psycopg2://username:password@localhost/pitch-V-2.0'
export SECRET_KEY='Your secret key'
```

### Run Database Migrations
```
python manage.py db init
python manage.py db migrate -m "initial migration"
python manage.py db upgrade
```

### Running the app in development
In the same terminal type:
`python3 manage.py server`

Open the browser on `http://localhost:5000/`

## Known bugs
SQLAlchemy errors, automatic sign out has a short time span

## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - JavaScript
    - Heroku
    - Postgresql

## Support and contact details
Contact me on gabrielcoder@gmail.com for any comments, reviews or advice.

### License
Copyright (c) **Gabriel Nwachukwu**