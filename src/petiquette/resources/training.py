from marshmallow.fields import (
    UUID,
)

from petiquette.directives import dbsession  # TODO


def commands():
    return []


def command(id: UUID()):
    return {}


def sessions(dbsession: dbsession):
    return []


def session(id: UUID()):
    return {}


def directives():
    return []


def directive(id: UUID()):
    return {}
