from models.database import Database
from typing import Self, Any, Optional

class Tarefa:
    def __init__(self: Self, titulo_tarefa: str, data_conclusão: str = None, id: int = None) -> None:
        self.titulo_tarefa: str = titulo_tarefa
        self.data_conclusao: str = data_conclusão
        self.id_tarefa: Optional[int] = id_tarefa
        self.id: int = id

    @classmethod
    def id(cls, id: int):
        with Database ('./data/tarefas.sqlite3') as db:
            query: str = 'SELECT titulo_tarefa, data_conclusao FROM tarefas WHERE id = ?;'
            params: tuple = (id,)
            resultado: list[Any] = db.buscar_tudo(query, params)

            [[titulo, data]] = resultado
        
        return cls(id_tarefa=id, tutulo_tarefa=titulo, data_conclusao=data)
       

    def salvar_tarefa(self: Self) -> None:
        with Database('./data/tarefas.sqlite3') as db:
         query: str = "INSERT INTO tarefas (titulo_tarefa, data_conclusao) VALUES (?, ?);"
        params: tuple = (self.titulo_tarefa, self.data_conclusao)
        db.executar(query, params)

    @staticmethod
    def obter_tarefa() -> list [Self]:
        with Database('./data/tarefas.sqlite3') as db:
          query = 'SELECT titulo_tarefa, data_conclusao FROM tarefas;'
          resultados = list[Any] = db.buscar_tudo (query)
          tarefas: list[Self] = [ Tarefa(titulo, data) for titulo, data in resultados]
          return tarefas 
        
    def excluir_tarefa(self) -> Cursor:
       with Database('./data/tarefas.sqlite3') as db:
          query: str = 'DELETE FROM tarefas WHERE id = ?;'
          params: tuple = (self )

