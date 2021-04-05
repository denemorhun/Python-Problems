# base configuration url for all test methods

import pytest
@pytest.fixture
def supply_url():
    return "http://reqres.in/api"