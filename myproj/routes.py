from . import resources


RESOURCES = {
    '/twitter/ids': resources.TwitterIDs

}


def add_resources(api):
    for path, resource in RESOURCES.items():
        api.add_resource(resource, path)
