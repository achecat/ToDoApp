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



