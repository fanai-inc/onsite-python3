from contextlib import suppress

import sqlalchemy as sa
from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Table,
)
from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base


engine = sa.create_engine('sqlite:///:memory:', echo=False)
Session = orm.sessionmaker(bind=engine)


Base = declarative_base()


def init_db():
    return Base.metadata.create_all(engine)


def deinit_db():
    return Base.metadata.drop_all(engine)


# https://stackoverflow.com/a/9119764
twitter_follows = Table(
    'twitter_follows', Base.metadata,
    Column('friend_id', ForeignKey('twitter_users.id'), primary_key=True),
    Column('follower_id', ForeignKey('twitter_users.id'), primary_key=True),
)


class TwitterUser(Base):
    __tablename__ = 'twitter_users'

    id = Column(Integer, primary_key=True)
    screen_name = Column(String, unique=True)
    followers_count = Column(Integer, default=0)
    friends_count = Column(Integer, default=0)
    is_public_figure = Column(Boolean, default=False)

    # many to many TwitterUser<->TwitterUser
    followers = orm.relationship(
        'TwitterUser',
        secondary=twitter_follows,
        primaryjoin=id == twitter_follows.c.friend_id,
        secondaryjoin=id == twitter_follows.c.follower_id,
        back_populates='friends',
    )
    friends = orm.relationship(
        'TwitterUser',
        secondary=twitter_follows,
        primaryjoin=id == twitter_follows.c.follower_id,
        secondaryjoin=id == twitter_follows.c.friend_id,
        back_populates='followers',
    )

    def follow(self, follower: 'TwitterUser'):
        """Twitter user wants to follow me."""
        if follower not in self.followers:
            self.followers.append(follower)
            self.followers_count = self.followers_count + 1
        if self not in follower.friends:
            follower.friends.append(self)
            follower.friends_count = follower.friends_count + 1

    def unfollow(self, follower: 'TwitterUser'):
        """Twitter user wants to unfollow me."""
        with suppress(ValueError):
            self.followers.remove(follower)
            self.followers_count = self.followers_count - 1
        with suppress(ValueError):
            follower.friends.remove(self)
            follower.friends_count = follower.friends_count - 1

    def friend(self, friend: 'TwitterUser'):
        """I want to follow a Twitter user."""
        friend.follow(self)

    def unfriend(self, friend: 'TwitterUser'):
        """I want to unfollow a Twitter user."""
        friend.unfollow(self)
