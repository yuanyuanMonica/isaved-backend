from app.__init__ import db

# from sqlalchemy import create_engine, MetaData
# from sqlalchemy.orm import scoped_session, sessionmaker
#
# engine = create_engine('sqlite:////tmp/test.db', convert_unicode=True)
# metadata = MetaData()
# db_session = scoped_session(sessionmaker(autocommit=False,
#                                          autoflush=False,
#                                          bind=engine))
# def init_db():
#     metadata.create_all(bind=engine)

db = db


class UserTagTable(db.Model):
    """ Initialize the user_tag_table from MySQL database

    +----------------+---------------+------+-----+---------+----------------+
    | Field          | Type          | Null | Key | Default | Extra          |
    +----------------+---------------+------+-----+---------+----------------+
    | userID         | int(11)       | NO   |     | NULL    |                |
    | itemID         | int(11)       | NO   | PRI | NULL    | auto_increment |
    | Link           | varchar(1000) | YES  |     | NULL    |                |
    | CreateTime     | datetime      | NO   |     | NULL    |                |
    | Tag            | varchar(1000) | YES  |     | NULL    |                |
    | Title          | varchar(1000) | YES  |     | NULL    |                |
    | LastUpdateTime | datetime      | NO   |     | NULL    |                |
    +----------------+---------------+------+-----+---------+----------------+
    """
    __tablename__ = 'user_tag'
    userID = db.Column(db.Integer, unique=False, nullable=False, primary_key=False)
    itemID = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    Link = db.Column(db.String(1000))
    Tag = db.Column(db.String(1000))
    Title = db.Column(db.String(1000))
    CreateTime = db.Column(db.DateTime)
    LastUpdateTime = db.Column(db.DateTime)

    # def __init__(self, userId, itemId):
    #     self.userID = userId
    #     self.itemID = itemId
    #
    # def __repr__(self):
    #     return "Tag {0} on {1}".format(self.userID, self.itemID)

