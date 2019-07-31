import importlib


def test__import_project(project_name):
    assert importlib.import_module(project_name)
