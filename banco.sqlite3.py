# exercicio masterclass basico, depois dos exercicios

import sqlite3

conexao = sqlite3.connect('bancodedados')

cursor = conexao.cursor()

sql = '''
create table pedido(
    id int not null,
    cliente varchar (100),
    data varchar (20), 
    primary key (id)
)
'''

cursor.execute(sql)
conexao.commit()
conexao.close()

# nao consegui a conexao






