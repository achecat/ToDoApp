from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

database = create_engine(
    "sqlite:///db/database.db",
    echo=True
    )


Base = declarative_base()

#perguntar o pq recomendam q o session seja o ultimo 
'''
Ordem de dependência: O sessionmaker precisa receber o bind=database (a engine de conexão). Portanto, a engine precisa ser criada antes dele.
'''


Session = sessionmaker(bind=database)