import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
MYSQL = {
    'default' : {
    'ENGINE' : 'django.db.backends.mysql',
    'OPTIONS': {
            # Tell MySQLdb to connect with 'utf8mb4' character set
            'charset': 'utf8mb4',
        },
        # Tell Django to build the test database with the 'utf8mb4' character set
        'TEST': {
            'CHARSET': 'utf8mb4',
            'COLLATION': 'utf8mb4_unicode_ci',
        },
    'NAME' : 'inventory',
    'USER': 'root',
    'PASSWORD' : '123',
    'HOST' : '127.0.0.1',
    'PORT' : '3306',
    'ATOMIC_REQUESTS': True
    }
}
POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'inventory',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True
    }
}
