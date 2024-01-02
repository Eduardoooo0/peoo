import sqlite3 as sql
con = sql.connect('Banco.db')
sql = con.cursor()
sql.execute('CREATE TABLE alunos (nome,nota1,nota2,nota3,nota4)')