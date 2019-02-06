# SPR Curve optmizer

This document is intended to help the users to install, configurate and run the SPR Curve optmizer application.

## Installation
Make a new Python virtual environment:
```sh
$ cd project_folder
$ python -m venv env
```
Activate the Python virtual environment:
- Windows:
```sh
$ env\Scripts\activate
```
- Linux:
```sh
$ env/bin/activate
```
Update the pip:
```sh
$ python -m pip install --upgrade pip
```

Install the requirements:
```sh
$ pip install -r requirements.txt
```

## Configuration

In the project root directory:
- Run the migrations as follows:

```sh
$ python manage.py migrate
```


Execute this command to run the application:
- python manage.py runserver 127.0.0.1:8080

Access the application:
-  http://localhost:8080