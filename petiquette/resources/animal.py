import random
import uuid
from dataclasses import field

import marshmallow as mm
from marshmallow.fields import (
    UUID,
)
from marshmallow_dataclass import dataclass
from typing import (
    ClassVar,
    Optional,
    Type,
)


DOG_TYPES_TO_ABBREVIATIONS = {
    'Australian Cattle Dog': 'ACD',
    'German Shepherd Dog': 'GSD',
    'Pomeranian': None,
}


@dataclass
class Dog:
    """Dog type contract."""
    id: str = field(metadata={'marshmallow_field': UUID()})
    name: str
    abbreviation: Optional[str]
    Schema: ClassVar[Type[mm.Schema]]


def dogs() -> Dog.Schema(many=True):
    return [
        Dog(id=uuid.uuid1(), name=name, abbreviation=abbrev)
        for name, abbrev in (
            random.choice(list(DOG_TYPES_TO_ABBREVIATIONS.items()))
            for idx in range(10)
        )
    ]


def dog(id: UUID()) -> Dog.Schema():
    name = random.choice(list(DOG_TYPES_TO_ABBREVIATIONS))
    abbrev = DOG_TYPES_TO_ABBREVIATIONS[name]
    return Dog(id=id, name=name, abbreviation=abbrev)
