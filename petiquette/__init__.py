import hug

from .api import router


@hug.extend_api()
def with_nested_apis():
    return [
        router.api,
    ]
