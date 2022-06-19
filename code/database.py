from tortoise import run_async, Tortoise

from .config import DATABASE_URL

TORTOISE_ORM = {
    'connections': {'default': DATABASE_URL},
    'apps': {
        'models': {
            'models': ['code.models', 'aerich.models'],
            'default_connection': 'default',
        },
    },
}


def connect_database():
    run_async(Tortoise.init(
        db_url=DATABASE_URL,
        modules={
            'models': ['code.models'],
        },
    ))
