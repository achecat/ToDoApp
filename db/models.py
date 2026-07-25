from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, Text, Date, DateTime
from db.database import Base, database

class Tarefa(Base):
    __tablename__ = "Tarefas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(100), nullable=False)
    descricao = Column(Text)
    categoria = Column(String(50), nullable=True, default="Geral")
    data = Column(Date, nullable=True)
    concluida = Column(Boolean, default=False, nullable=False)
    criada_em = Column(DateTime, default=datetime.now, nullable=False)

def criar_banco():
    Base.metadata.create_all(database)