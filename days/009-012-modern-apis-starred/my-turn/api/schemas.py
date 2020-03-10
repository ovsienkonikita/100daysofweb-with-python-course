import typing

import ujson
from marshmallow import Schema, fields, validate, ValidationError
from starlette.exceptions import HTTPException


class BaseSchema(Schema):
    def handle_error(self, error: ValidationError, data: typing.Any, *, many: bool, **kwargs):
        raise HTTPException(status_code=422, detail=ujson.dumps(error.messages))


class CharacterSchema(BaseSchema):
    pid = fields.Str(required=True)
    name = fields.Str(required=False)
    sid = fields.Str(required=False)
    align = fields.Str(required=False)
    sex = fields.Str(required=False, validate=validate.OneOf("Male Characters", "Female Characters"))
    appearances = fields.Int(required=False)
    year = fields.Str(required=False)
