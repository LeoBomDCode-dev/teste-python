from models.database import Database

# Teste do gerenciador de contexto 
with Database('./data/tarefas.sqlite3') as db:
    db.executar(
        'INSERT TEXTO tarefas (titulo_tarefa, data_conclusao) VALUES (?, ?):',
    ('usar o gerenciador de contexto', '2026-02-03'))