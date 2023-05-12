import pytest


@pytest.mark.usefixtures("get_browser")
class BaseClass:
    pass
