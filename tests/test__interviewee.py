import pytest


def test__twitter_users(client, dbsession, models):
    # GIVEN 1,000 Twitter users exist in the database
    NUM_TWITTER_USERS = 1_000
    for idx in range(NUM_TWITTER_USERS):
        dbsession.add(models.TwitterUser(
            screen_name=f'handle_{idx}',
            followers_count=0,
            friends_count=0,
            is_public_figure=True,
        ))
    dbsession.commit()

    # WHEN all Twitter IDs are requested
    resp = client.get('/twitter/ids')

    # THEN 1,000 IDs are returned
    assert len(resp.json) == NUM_TWITTER_USERS, resp.json
    assert all(isinstance(id_, int) for id_ in resp.json), resp.json


@pytest.mark.first
def test__first_requirement(client):
    # GIVEN
    pass

    # WHEN

    # THEN


@pytest.mark.second
def test__second_requirement(client):
    # GIVEN
    pass

    # WHEN

    # THEN


@pytest.mark.third
def test__third_requirement(client):
    # GIVEN
    pass

    # WHEN

    # THEN
