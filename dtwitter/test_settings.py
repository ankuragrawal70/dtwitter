db_name, db_user, db_password, db_host = "dwitter", "root", "root", "localhost"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': db_password,
        'HOST': db_host,
        'PORT': '',
    },
}