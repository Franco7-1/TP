from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), unique=True)
    usuario = relationship("Usuario")

    def presentarse(self):
        return f"Hola, soy el cliente {self.usuario.nombre}"
