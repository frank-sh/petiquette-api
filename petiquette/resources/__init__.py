__all__ = [
    'commands', 'command',
    'directives', 'directive',
    'dogs', 'dog',
    'pets', 'pet',
    'sessions', 'session',
    'trainers', 'trainer',
]


from .animal import (
    dogs, dog,
)
from .pet import (
    pets, pet,
    trainers, trainer,
)
from .training import (
    commands, command,
    directives, directive,
    sessions, session,
)
