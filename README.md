# Teamway


Build a REST application from scratch that could serve as a work planning service.


Business requirements:
 - A worker has shifts
 - A shift is 8 hours long
 - A worker never has two shifts on the same day
 - It is a 24 hour timetable 0-8, 8-16, 16-24



### Virtual Environment Setup

    virtualenv venv -p python3

#### Activate Virtual environment

    source venv/bin/activate

#### Install requirements

    pip install -r requirements.txt


### Django Migrations

#### Create migrations

    python manage.py makemigrations

#### Run Migrations

    python manage.py migrate


#### Run Test

    python manage.py test
