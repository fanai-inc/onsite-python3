import pytest


def test__twitter_users(client, dbsession, models):
    # GIVEN 1,000 Twitter users exist in the database
    NUM_TWITTER_USERS = 1_000
    for idx in range(NUM_TWITTER_USERS):
        dbsession.add(models.TwitterUser(
            screen_name=f'handle_{idx}',
            is_public_figure=True,
        ))
    dbsession.commit()

    # WHEN all Twitter IDs are requested
    resp = client.get('/twitter/ids')
    assert resp.status_code == 200, resp.json

    # THEN 1,000 IDs are returned
    assert len(resp.json) == NUM_TWITTER_USERS, resp.json
    assert all(isinstance(id_, int) for id_ in resp.json), resp.json


def test__followers_count(client, dbsession, models):
    # GIVEN a Twitter user with 1,000 followers
    NUM_FOLLOWERS = 1_000
    public_figure = models.TwitterUser(
        screen_name='first_public_figure',
        is_public_figure=True,
    )
    dbsession.add(public_figure)
    dbsession.flush()
    users = [
        models.TwitterUser(screen_name=f'handle_{idx}')
        for idx in range(NUM_FOLLOWERS)
    ]
    dbsession.add_all(users)
    for user in users:
        public_figure.follow(user)
    dbsession.commit()

    # WHEN the count of this user's followers is requested
    resp = client.get(f'/twitter/{public_figure.id}/followers/count')
    assert resp.status_code == 200, resp.json

    # THEN 1,000 is returned
    assert resp.json == NUM_FOLLOWERS, resp.json


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
