from uuid import uuid4

import sqlalchemy as sa
from constatns import blood_groups
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import validates, relationship

from . import Base


class Donor(Base):
    __tablename__ = "donors"

    id_ = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False)
    blood_group = sa.Column(sa.String)
    medical_report = sa.Column(sa.String)
    adress = sa.Column(sa.String)
    phone_number = sa.Column(sa.Integer)

    blood_bank_id = sa.Column(sa.Integer, sa.ForeignKey("blood_banks.id_"))
    blood_bank = relationship("BloodBank")

    # TODO move to BloodGroupMixin
    @validates("blood_group")
    def validate_blood_group(self, key, adress):
        assert adress in blood_groups
        return adress
