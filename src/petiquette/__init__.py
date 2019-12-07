import hug

from .api import router
from .context import Context


@hug.context_factory()
def create_context(*args, **kwargs):
    return Context()


@hug.delete_context()
def delete_context(context: Context,
                   exception=None, errors=None, lacks_requirements=None):
    context.cleanup(exception)


@hug.directive()
def dbsession(context: Context):
    return context.dbsession


@hug.extend_api()
def with_nested_apis():
    return [
        router.api,
    ]
