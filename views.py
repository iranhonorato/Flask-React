# Arquivo de funções que executaram comandos sql nas rotas

import sqlite3 as sql 
import utils

def get_all_posts():
    conn = utils.connect_db() 
    cursor = conn.cursor()
    sql = "SELECT * FROM posts"
    cursor.execute(sql)

    data = cursor.fetchall(sql)
    conn.close()

    return data



def get_post(id):
    conn = utils.connect_db()
    cursor = conn.cursor()
    sql = "SELECT * FROM posts WHERE id = ?"         # Essa formatação impede sql injection
    cursor.execute(sql, (id, ))

    data = cursor.fetchone()
    conn.close()

    return data 



def create_post(title, content):
    conn = utils.connect_db() 
    cursor = conn.cursor()
    sql = "INSERT INTO posts (title, content) VALUES (?, ?)"
    cursor.execute(sql, (title, content))
    conn.commit()
    conn.close()




