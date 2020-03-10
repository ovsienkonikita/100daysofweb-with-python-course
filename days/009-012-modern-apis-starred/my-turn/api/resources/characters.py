from starlette.requests import Request
from starlette.responses import UJSONResponse

from . import BaseResource
from ..database import db
from ..models import Character
from ..schemas import CharacterSchema


class CharactersResource(BaseResource):
    schema = CharacterSchema()

    async def get(self, request):
        return UJSONResponse(self.schema.dump(db.values(), many=True))

    async def post(self, request: Request):
        data = await request.json()
        data = self.schema.load(data)
        character = Character(**data)
        db.add_character(character)
        return UJSONResponse(self.schema.dump(character), 201)
