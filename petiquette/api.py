__all__ = [
    'router',
]

import hug

from . import resources


CLI = 'CLI'
GET = 'GET'
POST = 'POST'
PUT = 'PUT'
PATCH = 'PATCH'
DELETE = 'DELETE'
OPTIONS = 'OPTIONS'

router = hug.route.API(__name__)

"""
www.petiquette.com/<profile>
api.petiquette.com/v0/pets

/auth/user
/types/animals
/types/animals/{id}
/types/dogs
/types/dogs/{id}
/training/commands
/training/commands/{id}
/training/sessions
/training/sessions/{id}
/training/sessions/{id}/commands
/training/sessions/commands
/pets
/pets/{id}
/trainers
/trainers/{id}

"""
routes = {
    '/commands': {},
    '/commands/{id}': {},
    '/dogs': {GET: resources.dogs},
    '/dogs/{id}': {GET: resources.dog},
    '/directives': {},
    '/directives/{id}': {},
    '/pets': {},
    '/pets/{id}': {},
    '/sessions': {},
    '/sessions/{id}': {},
    '/trainers': {},
    '/trainers/{id}': {},
    '/users': {},
    '/users/{id}': {},
}

for path, resource_by_method in routes.items():
    for accept_methods, resource in resource_by_method.items():
        if not isinstance(accept_methods, (tuple, list)):
            accept_methods = (accept_methods,)
        router.cli()(resource)
        router.http(path, accept=accept_methods)(resource)
