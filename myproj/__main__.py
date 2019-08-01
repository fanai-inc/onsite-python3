from . import factory
from .models import init_db


app = factory.create_app()


if __name__ == '__main__':
    init_db()
    app.run()
