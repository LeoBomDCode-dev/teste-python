from sqlite3 import Connection, connect, Cursor
from types import TracebackType
from typing import Any, Self, Optional, Type
import traceback

class Database:
     def __init__(self, db_name: str) -> None:
         self.connection: Connection = connect(db_name)
         self.cursor: Cursor = self.connection.cursor()

     def executar(self, query: str, params: tuple = ()) -> Cursor:
         self.cursor.execute(query, params)
         self.connection.commit()
         return self.cursor
     
     
     def buscar_tudo(self, query:str, params: tuple = ()) -> list[Any]:
         self.cursor.execute(query, params)
         return self.cursor.fetchall()

    
def close(self) -> None:
    self.connection.close()

    #Area testes

# try:
#     db = Database('./data/tarefas.sqlite3')
#     db.executar('')


def __enter__(self) -> Self:
    print('Entrando no contexto...')
    return self

def __exit__(self, exc_type, exc_value, teaceback) -> None:

    if exc_type is not None:
        print('Exceção capturada no contexto:')
        print(f'Tipo: {exc_type.__name__}')
        print(f'Mensagem: {exc_value}')
        print('Traceback completo:')
        traceback.print_tb(tb)

    self.close()

    