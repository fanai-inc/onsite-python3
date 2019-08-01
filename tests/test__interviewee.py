import pytest


@pytest.mark.first
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


@pytest.mark.second
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


@pytest.mark.third
def test__first_requirement(client, dbsession, models):
    # GIVEN at least 2 public figures with shared followers
    NUM_LEFT, NUM_SHARED, NUM_RIGHT = 400, 982, 523
    left, right = (
        models.TwitterUser(
            screen_name=f'public_figure_{idx}',
            is_public_figure=True,
        ) for idx in range(2)
    )
    dbsession.add_all([left, right])
    dbsession.flush()
    left_users = [
        models.TwitterUser(screen_name=f'left_follower_{idx}')
        for idx in range(NUM_LEFT)
    ]
    shared_users = [
        models.TwitterUser(screen_name=f'shared_follower_{idx}')
        for idx in range(NUM_SHARED)
    ]
    right_users = [
        models.TwitterUser(screen_name=f'right_follower_{idx}')
        for idx in range(NUM_RIGHT)
    ]
    dbsession.add_all(left_users)
    dbsession.add_all(shared_users)
    dbsession.add_all(right_users)
    for user in left_users:
        left.follow(user)
    for user in shared_users:
        left.follow(user)
        right.follow(user)
    for user in right_users:
        right.follow(user)

    # WHEN
    resp = client.get(f'/twitter/followers/intersect/{left.id}/{right.id}')
    assert resp.status_code == 200

    # THEN
    assert resp.json == len(shared_users)


@pytest.mark.fourth
def test__second_requirement(client):
    # GIVEN
    pass

    # WHEN

    # THEN


@pytest.mark.fifth
def test__third_requirement(client):
    # GIVEN
    pass

    # WHEN

    # THEN
