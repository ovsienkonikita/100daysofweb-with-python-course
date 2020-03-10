from collections import UserDict
from typing import Dict

from starlette.exceptions import HTTPException

from api.parsers import create_parser
from .models import Character


class __Database(UserDict):
    def init_data(self, file_path: str) -> Dict:
        parser = create_parser(file_path)
        data = parser()
        for character in data:
            self.data[character.pid] = character

    def add_character(self, character: Character):
        if character.pid in self.data:
            raise HTTPException(400, detail="Character with same pid already exist")
        self.data[character.pid] = character

    def get_character(self, pid: str) -> Character:
        character = self.get(pid)
        if not character:
            raise HTTPException(404, detail="Character not found")
        return character

    def update_character(self, pid: str, **data) -> Character:
        character = self.get_character(pid)
        character._replace(**data)  # shit
        return character

    def delete_character(self, pid) -> bool:
        return bool(self.pop(pid))


db = __Database()
