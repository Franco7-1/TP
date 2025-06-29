from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Empleado(Base):
    __tablename__ = 'empleados'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), unique=True)
    puesto = Column(String(50))
    usuario = relationship("Usuario")

    def presentarse(self):
        return f"Hola, soy el empleado {self.usuario.nombre}, puesto: {self.puesto}"
