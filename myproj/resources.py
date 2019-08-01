from flask.json import jsonify
from flask_restful import Resource

from .models import (
    engine,
    Session,
    TwitterUser,
)


class TwitterIDs(Resource):

    def get(self):
        conn = engine.connect()
        query = conn.execute('''
            SELECT id
            FROM twitter_users
        ''')
        return jsonify([id_ for id_, *_ in query.cursor.fetchall()])


class TwitterFollowersCount(Resource):

    def get(self, id):
        dbsession = Session()
        user = dbsession.query(TwitterUser).get(id)
        return jsonify(user.followers_count)
