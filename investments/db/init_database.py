import sqlite3


def init_database(database_name: str):
    connection = sqlite3.connect(database_name)
    db = connection.cursor()
    db.execute("""CREATE TABLE IF NOT EXISTS 'USD' (
                'date'	INTEGER NOT NULL UNIQUE,
                'rate'	REAL NOT NULL
                );""")

    db.execute("""CREATE TABLE IF NOT EXISTS 'GOLD' (
                'date'	INTEGER NOT NULL UNIQUE,
                'rate'	REAL NOT NULL
                );""")

    db.execute("""CREATE TABLE IF NOT EXISTS 'AAPL' (
                'date'	INTEGER NOT NULL UNIQUE,
                'rate'	REAL NOT NULL
                );""")

    db.execute("""CREATE TABLE IF NOT EXISTS 'FB' (
                'date'	INTEGER NOT NULL UNIQUE,
                'rate'	REAL NOT NULL
                );""")

    db.execute("""CREATE TABLE IF NOT EXISTS 'BA' (
                'date'	INTEGER NOT NULL UNIQUE,
                'rate'	REAL NOT NULL
                );""")

    db.execute("""CREATE TABLE IF NOT EXISTS 'BTC' (
                'date'	INTEGER NOT NULL UNIQUE,
                'rate'	REAL NOT NULL
                );""")

    db.execute("""CREATE TABLE IF NOT EXISTS 'EUR' (
                'date'	INTEGER NOT NULL UNIQUE,
                'rate'	REAL NOT NULL
                );""")

    connection.commit()
    connection.close()
