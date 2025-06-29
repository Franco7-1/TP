from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .base import Base
from utils.tiempo import fecha_argentina

class Venta(Base):
    __tablename__ = 'ventas'
    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    empleado_id = Column(Integer, ForeignKey('empleados.id'))
    monto = Column(Float)
    fecha = Column(DateTime, default=fecha_argentina)

    cliente = relationship("Cliente")
    empleado = relationship("Empleado")
