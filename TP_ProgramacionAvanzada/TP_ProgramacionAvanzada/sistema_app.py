from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from db import crear_engine
from models import Usuario, Cliente, Empleado, Venta

class SistemaApp:
    def __init__(self, db_url='sqlite:///sistema.db'):
        self.engine = crear_engine(db_url)

    def insertar_usuarios(self, lista_usuarios):
        insertados = []
        with Session(self.engine) as session:
            emails_existentes = set(row[0] for row in session.query(Usuario.email).all())
            for datos in lista_usuarios:
                if datos["email"] in emails_existentes:
                    print(f"Email duplicado: {datos['email']}")
                    continue

                usuario = Usuario(
                    email=datos["email"],
                    nombre=datos["nombre"],
                    edad=datos["edad"],
                    sexo=datos["sexo"],
                    telefono=datos.get("telefono")
                )
                session.add(usuario)
                session.flush()

                if datos["tipo"] == "cliente":
                    session.add(Cliente(usuario_id=usuario.id))
                elif datos["tipo"] == "empleado":
                    session.add(Empleado(usuario_id=usuario.id, puesto=datos["puesto"]))

                try:
                    session.commit()
                    insertados.append(usuario)
                except IntegrityError:
                    session.rollback()
                    print(f"Error al insertar: {usuario.email}")
        return insertados

    def mostrar_clientes(self):
        with Session(self.engine) as session:
            clientes = session.query(Cliente).all()
            print("\nTabla de Clientes:")
            print("┌────┬──────────────────────────────┬──────────────────────┬──────┬──────┬──────────────┐")
            print("│ ID │           EMAIL              │        NOMBRE        │ EDAD │ SEXO │   TELEFONO   │")
            print("├────┼──────────────────────────────┼──────────────────────┼──────┼──────┼──────────────┤")
            for c in clientes:
                u = c.usuario
                print(f"│ {c.id:2} │ {u.email:28} │ {u.nombre:20} │ {u.edad:3}  │   {u.sexo}  │ {u.telefono or 'N/A':12} │")
            print("└────┴──────────────────────────────┴──────────────────────┴──────┴──────┴──────────────┘")

    def mostrar_empleados(self):
        with Session(self.engine) as session:
            empleados = session.query(Empleado).all()
            print("\nTabla de Empleados:")
            print("┌────┬──────────────────────────────┬──────────────────────┬──────┬──────┬────────────────┬──────────────┐")
            print("│ ID │           EMAIL              │        NOMBRE        │ EDAD │ SEXO │     PUESTO     │   TELEFONO   │")
            print("├────┼──────────────────────────────┼──────────────────────┼──────┼──────┼────────────────┼──────────────┤")
            for e in empleados:
                u = e.usuario
                print(f"│ {e.id:2} │ {u.email:28} │ {u.nombre:20} │ {u.edad:3}  │   {u.sexo}  │ {e.puesto:14} │ {u.telefono or 'N/A':12} │")
            print("└────┴──────────────────────────────┴──────────────────────┴──────┴──────┴────────────────┴──────────────┘")

    def registrar_venta(self, cliente_id, empleado_id, monto):
        with Session(self.engine) as session:
            venta = Venta(cliente_id=cliente_id, empleado_id=empleado_id, monto=monto)
            session.add(venta)
            session.commit()
            print(f"\nVenta registrada: Cliente {cliente_id} - Empleado {empleado_id} - Monto ${monto}")

    def mostrar_ventas(self):
        with Session(self.engine) as session:
            ventas = session.query(Venta).all()
            print("\nVentas registradas:")
            for v in ventas:
                print(f"Venta ID: {v.id} | Cliente: {v.cliente.usuario.nombre} | Empleado: {v.empleado.usuario.nombre} | "
                      f"Monto: ${v.monto} | Fecha (ARG): {v.fecha.strftime('%Y-%m-%d %H:%M:%S')}")
