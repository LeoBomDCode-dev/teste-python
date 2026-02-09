from flask import Flask, render_template, request, redirect, url_for
from models.tarefa import Tarefa

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html', titulo='home')

@app.route('/agenda', methods= ['GET', 'POST'])
def agenda():
   tarefa = None
   
   if request.method == 'POST':
      titulo_tarefa = request.form['titulo_tarefa']
      data_conclusao = request.form['data-conclusao']
      tarefa = Tarefa(titulo_tarefa, data_conclusao)
      tarefa.salvar_tarefa()

   tarefas = Tarefa.obter_tarefa()
   return render_template('base.html', titulo='Agenda',tarefas=tarefas)

@app.route('/delete/clint:idTarefa>')
def delete(idTarefa):
   tarefa = Tarefa.id(idTarefa)
   tarefa.excluir_tarefa()
   return redirect(url_for('agenda'))

@app.route('/update/<int:idTarefa>', methods=["GET", 'POST'])
def update(idTarefa):

   if request.method == 'POST':
      titulo = request.form['titulos-tarefa']
      data = request.form['data=conclusao']
      tarefa = Tarefa (titulo, data, idTarefa)
      tarefa.atualizar_tarefa()
      return redirect(url_for('agenda')) #early return


   tarefas = Tarefa.obter_tarefas()
   tarefa_selecionadas = Tarefa.id(idTarefa)
   
   return render_template('agenta.html', titulo=f"Editando a tarefa ID: {idTarefa}",
   tarefas=tarefas, tarefa_selecionada=tarefa_selecionadas)


@app.route('/ola')
def ola_mundo():
    return "Olá, Mundo!"