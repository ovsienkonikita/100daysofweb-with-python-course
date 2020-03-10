import pytest
import asyncio

from starlette.testclient import TestClient

from api.api import api, init_database


@pytest.fixture(scope="session")
def test_client():
    asyncio.run(init_database())  # dirty hack, idk why it's not working without that
    return TestClient(api)
