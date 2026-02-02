# from sqlite3 import Connection, connect, Cursor

# class Database:
#     def __init__(self, db_name: str) -> None:
#         self.connection: Connection = connect(db_name)
#         self.cursor: Cursor = self.connection.cursor()

#     def executar(self, query: str, params: tuple = ()) -> Cursor:
#         self.cursor.execute(query, params)
#         self.connection.commit()
#         return self.cursor
#     def buscar_tudo(self, query:str, params: tuple = ()):
#         self.cursor.execute(query, params)
#         return self.cursor.fetchall()

def 
    
def close(self) -> None:
    self.connection.close()

    #Area testes

# try:
#     db = Database('./data/tarefas.sqlite3')
#     db.executar('')


def __enter__(self):
    print('Entrando no contexto...')
    return self

def __exit__(self, exc_type, exc_value, teaceback):
    print('Saindo do contexto...')
    self.close()