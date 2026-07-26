from db.database import Session
from db.models import Tarefa

class ServiceTarefas:

    @staticmethod
    def adicionar(titulo, descricao=None, categoria="Geral", data=None):
        session = Session()

        nova_tarefa = Tarefa(
            titulo = titulo,
            descricao = descricao,
            categoria = categoria,
            data = data
        )

        session.add(nova_tarefa)
        session.commit()
        session.close()


    @staticmethod
    def listar_todas():
        session = Session()

        tarefas = session.query(Tarefa).all()

        session.close()

        return tarefas


    @staticmethod
    def alternar_status(tarefa_id):
        session = Session()

        tarefa = session.query(Tarefa).filter_by(id=tarefa_id).first()

        if tarefa:
            tarefa.concluida = not tarefa.concluida
            session.commit()

        session.close()


    @staticmethod
    def deletar_tarefa(tarefa_id):
        session = Session()

        tarefa = session.query(Tarefa).filter_by(id=tarefa_id).first()

        if tarefa:
            session.delete(tarefa)
            session.commit()

        session.close()