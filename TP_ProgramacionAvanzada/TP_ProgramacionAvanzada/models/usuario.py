from sqlalchemy import Column, Integer, String
from .base import Base

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    nombre = Column(String(50), nullable=False)
    edad = Column(Integer)
    sexo = Column(String(1))
    telefono = Column(String(20))

