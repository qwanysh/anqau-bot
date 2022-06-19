import logging

from .app import app
from .config import HEROKU_APP_NAME, HEROKU_PORT, TOKEN
from .database import connect_database

WEBHOOK_URL_TEMPLATE = 'https://{}.herokuapp.com/{}'

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)


def main():
    connect_database()

    if HEROKU_APP_NAME:
        app.run_webhook(
            listen='0.0.0.0',
            port=int(HEROKU_PORT),
            url_path=TOKEN,
            webhook_url=WEBHOOK_URL_TEMPLATE.format(
                HEROKU_APP_NAME, TOKEN,
            ),
        )
    else:
        app.run_polling()


if __name__ == '__main__':
    main()
