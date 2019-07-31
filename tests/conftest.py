import pytest


@pytest.fixture(scope='session')
def project_name():
    import myproj

    yield myproj.__name__
