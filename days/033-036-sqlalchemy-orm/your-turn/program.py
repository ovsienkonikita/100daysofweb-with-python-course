from app.infrastructure.switchlang import switch
from app.db import session_factory


def main():
    setup_db()

    options = "[h]elp \n"
    cmd = "NO CMD"
    while cmd:
        cmd = input(options).lower().strip()
        with switch(cmd) as s:
            s.default(lambda: print(f"Unknown comand: {cmd}"))


def setup_db():
    session_factory.global_init("blood_donation.sqlite")
    session_factory.create_tables()
    # import_data.import_if_empty()


if __name__ == "__main__":
    main()
