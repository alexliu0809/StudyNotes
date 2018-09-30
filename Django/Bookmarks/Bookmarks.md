# Building A Social Network
# Start A New Project And App
```shell
django-admin startproject bookmarks
cd bookmarks
django-admin startapp account
```

Register account app in the project by adding 'account' to settings.py.
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
]
```

Migrate
```shell
python manage.py migrate
```

# Djano Authentication Framework