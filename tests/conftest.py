import pytest


@pytest.fixture(scope='session')
def project_name():
    import myproj

    yield myproj.__name__


@pytest.fixture
def app():
    from myproj.factory import create_app

    yield create_app()


@pytest.fixture
def config(app):
    yield app.config


@pytest.fixture(scope='session')
def models():
    import myproj.models

    yield myproj.models


@pytest.fixture
def dbengine(models):
    models.init_db()
    yield models.engine
    models.deinit_db()


@pytest.fixture
def dbsession(models, dbengine):
    models.Session.configure(bind=dbengine)
    session = models.Session()
    try:
        yield session
    finally:
        session.close()
