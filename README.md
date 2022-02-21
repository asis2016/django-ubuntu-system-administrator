# Django Ubuntu System Administration (DUSA)

Django Ubuntu System Administration is a web application built on Django Web Framework. The web application provides web interface to manage and monitor Ubuntu server.

Project status: WIP

# Installation

```
$ mkdir new-project
$ cd new-project
```

```
$ git clone https://github.com/asis2016/django-ubuntu-system-administrator.git .
```

```
new-project $ python3 -m venv venv
new-project $ source venv/bin/activate
(venv) new-project $ pip install -r requirements.txt
```

```
(venv) new-project/project $ python3 manage.py runserver
```

Now, browse to http://localhost:8000

## Implementation (WIP)

### $ df / -h
Displays file system disk space usage.

![](screenshots/1.png)