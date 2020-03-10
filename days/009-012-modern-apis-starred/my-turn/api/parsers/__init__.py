from .csv_parser import CSVParser

parser_map = {"csv": CSVParser}


def create_parser(file_name: str):
    file_extension = file_name.split(".")[-1]
    parser = parser_map[file_extension](file_name)
    return parser
