import sqlite3 as sql 



# Estabelencendo uma conexão com o banco de dados SQLite
conn = sql.connect("data_base.db")



# Declarando um cursor para posterior interação como banco de dados
cursor = conn.cursor()




# Verificando se já existe um banco de dados com o nome que queremos criar 
cursor.execute("DROP TABLE IF EXISTS posts")





# Criando a tabela "posts" no nosso banco de dados "data_base.db"

sql = ''' CREATE TABLE "posts" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "title" TEXT NOT NULL, 
    "content" TEXTE NOT NULL
)'''

cursor.execute(sql)





# Salvando as alterações feitas 
conn.commit() 




# Finalizando a conexão com o banco de dados
conn.close()