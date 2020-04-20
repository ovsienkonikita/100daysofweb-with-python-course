import sqlalchemy as sa
from constatns import blood_groups
from sqlalchemy.orm import validates

from . import Base


class Patinet(Base):
    __tablename__ = "patients"

    id_ = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False)
    blood_group = sa.Column(sa.String)
    disease = sa.Column(sa.String)

    @validates("blood_group")
    def validate_blood_group(self, key, adress):
        assert adress in blood_groups
        return adress
