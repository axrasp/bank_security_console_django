# Bank security console

The code allows you to monitor visits in real time, keep a registry and determine which of them are suspicious.

## How to install

Python3 should be already installed. Then use ``pip`` (or ``pip3``, if there is a conflict with Python2) to install dependencies:

```
pip install -r requirements.txt
```
Now we need to connect your database.

Сreate ``.env`` file in ``project`` folder and put sensitive data there:

```
DATABASES_ENGINE="django.db.backends.postgresql_psycopg2"

DATABASES_HOST="example.org"

DATABASES_PORT="5434"

DATABASES_NAME="example"

DATABASES_USER="example"

DATABASES_PASSWORD="example"

DEBUG="True"

ALLOWED_HOSTS=127.0.0.1,localhost

SECRET_KEY="REPLACE_ME"
```

``DEBUG`` setting allows you to launch code in Debug mode:

https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-DEBUG

## Launching 

Start the code by following command:

```
python manage.py runserver 0.0.0.0:8000
```

Now Security Console is available right here:

http://0.0.0.0:8000


## Project Goals
The code is written for educational purposes on online-course for web-developers dvmn.org.