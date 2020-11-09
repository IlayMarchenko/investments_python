import sqlite3


def add_to_db(table: str, date: int, rate: float):
    connection = sqlite3.connect('db/database.db')
    db = connection.cursor()
    values_list = [(date, rate)]
    db.executemany(f"INSERT INTO {table.upper()} (date, rate) VALUES ( ? , ? )", values_list)
    connection.commit()
    connection.close()
