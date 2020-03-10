import csv
import re
from typing import Iterator
from datetime import date

from ..models import Character


class CSVParser:
    def __init__(self, file_name):
        self.file_name = file_name

    def __call__(self, *args, **kwargs) -> Iterator:
        with open(self.file_name) as csvfile:
            for row in csv.DictReader(csvfile):
                name = re.sub(r"(.*?)\(.*", r"\1", row["name"]).strip()
                yield Character(
                    pid=row["page_id"],
                    name=name,
                    sid=row["ID"] or None,
                    align=row["ALIGN"] or None,
                    sex=row["SEX"] or None,
                    appearances=row["APPEARANCES"] or None,
                    year=row["Year"] or None,
                )
