from sqlalchemy.engine import create_engine
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker


db_engine = create_engine('sqlite:///:memory:', echo=True)
DBSession = scoped_session(sessionmaker(bind=db_engine))


class Context:
    __slots__ = ('dbsession',)

    def __init__(self):
        self.dbsession = DBSession()

    def cleanup(self, exception=None):
        if exception:
            self.dbsession.rollback()
        else:
            self.dbsession.commit()
        DBSession.remove()
