from marshmallow.fields import (
    UUID,
)


def pets():
    return []


def pet(id: UUID()):
    return {'id': id}


def trainers():
    return []


def trainer(id: UUID()):
    return {'id': id}
