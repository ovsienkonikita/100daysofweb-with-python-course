from starlette.requests import Request
from starlette.responses import PlainTextResponse, UJSONResponse, Response

from . import BaseResource
from ..database import db
from ..schemas import CharacterSchema


class CharacterResource(BaseResource):
    schema = CharacterSchema()

    async def get(self, request: Request):
        character = db.get_character(request.path_params["pid"])
        return UJSONResponse(self.schema.dump(character), 200)

    async def patch(self, request: Request):
        pid = request.path_params["pid"]
        data = await request.json()
        data = self.schema.load({"pid": pid, **data})
        character = db.update_character(**data)
        return UJSONResponse(self.schema.dump(character), 200)

    async def delete(self, request: Request):
        pid = request.path_params["pid"]
        status = db.delete_character(pid)
        return Response(status_code=204) if status else PlainTextResponse("Character not found")
