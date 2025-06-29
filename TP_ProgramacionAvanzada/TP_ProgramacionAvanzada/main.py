from sistema_app import SistemaApp

if __name__ == "__main__":
    app = SistemaApp()

    usuarios = [
        {"email": "cliente1@correo.com", "nombre": "María López", "edad": 28, "sexo": "F", "telefono": "1133224455", "tipo": "cliente"},
        {"email": "empleado1@empresa.com", "nombre": "Pedro Salas", "edad": 40, "sexo": "M", "telefono": "1122334455", "tipo": "empleado", "puesto": "Vendedor"},
        {"email": "cliente2@correo.com", "nombre": "Carlos Ruiz", "edad": 35, "sexo": "M", "telefono": "1144556677", "tipo": "cliente"},
        {"email": "empleado2@empresa.com", "nombre": "Laura Vega", "edad": 30, "sexo": "F", "telefono": "1199887766", "tipo": "empleado", "puesto": "Asistente"},
        {"email": "cliente1@correo.com", "nombre": "Duplicado", "edad": 99, "sexo": "F", "telefono": "1000000000", "tipo": "cliente"}
    ]

    nuevos = app.insertar_usuarios(usuarios)
    print(f"\nSe insertaron {len(nuevos)} nuevos usuarios.\n")

    app.mostrar_clientes()
    app.mostrar_empleados()
    app.registrar_venta(cliente_id=1, empleado_id=1, monto=1500.50)
    app.mostrar_ventas()
