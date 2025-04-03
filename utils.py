# Arquivo de funções auxiliares

import sqlite3 as sql


def connect_db():
    conn = sql.connect("data_base.db")
    return conn