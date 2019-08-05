from dataclasses import field

import marshmallow as mm
from marshmallow.fields import (
    UUID,
)
from marshmallow_dataclass import dataclass
from typing import (
    ClassVar,
    Type,
)


@dataclass
class Pet:
    """Pet contract."""
    id: str = field(metadata={'marshmallow_field': UUID()})
    type: str
    Schema: ClassVar[Type[mm.Schema]] = mm.Schema


def pets():
    return []


def pet(id: UUID()):
    return {'id': id}


def trainers():
    return []


def trainer(id: UUID()):
    return {'id': id}
