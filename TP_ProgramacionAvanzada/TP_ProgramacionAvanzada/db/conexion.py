from sqlalchemy import create_engine
from models import Base

def crear_engine(db_url='sqlite:///sistema.db'):
    engine = create_engine(db_url, echo=False)
    Base.metadata.create_all(engine)
    return engine
