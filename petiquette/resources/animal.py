from marshmallow.fields import (
    UUID,
)


def dogs():
    return []


def dog(id: UUID()):
    return {'id': str(id)}
