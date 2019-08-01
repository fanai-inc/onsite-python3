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


twitter_follows = Table(
    'twitter_follows', Base.metadata,
    Column('friend_id', ForeignKey('twitter_users.id'), primary_key=True),
    Column('follower_id', ForeignKey('twitter_users.id'), primary_key=True),
)


class TwitterUser(Base):
    __tablename__ = 'twitter_users'

    id = Column(Integer, primary_key=True)
    screen_name = Column(String, unique=True)
    followers_count = Column(Integer)
    friends_count = Column(Integer)
    is_public_figure = Column(Boolean)

    # many to many TwitterUser<->TwitterUser
    followers = orm.relationship('TwitterUser', secondary=twitter_follows,
                                 foreign_keys=[twitter_follows.c.follower_id])
    friends = orm.relationship('TwitterUser', secondary=twitter_follows,
                               foreign_keys=[twitter_follows.c.friend_id])
