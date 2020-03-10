import os

from starlette.applications import Starlette
from starlette.routing import Route, Mount
from .resources import SmokeResource
from .resources.character import CharacterResource
from .resources.characters import CharactersResource
from .database import db


async def init_database():
    file_path = os.path.join(os.path.dirname(__file__), "static/marvel-wikia-data.csv")
    db.init_data(file_path)


routes = [
    Route("/smoke", SmokeResource),
    Mount(
        "/characters",
        routes=[
            Route("/", CharactersResource, methods=["GET", "POST"]),
            Route("/{pid}", CharacterResource, methods=["GET", "POST", "PATCH", "DELETE"]),
        ],
    ),
]

api = Starlette(debug=True, routes=routes, on_startup=[init_database])
