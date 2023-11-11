
import psycopg2
import sys
from listado.listado import listado
config = {
    "user": "postgres",
    "password": "pwd2023",
    "host": "localhost",
    "dbname": "listado",
}

if len(sys.argv) < 2:
    print(
        "Uso: python3 application.py [--listado |] <comando> [...]"
    )
else:
    try:
        if sys.argv[1] == "--listado":
            listado = listado(config)
            ubcomando = sys.argv[2]
            if subcomando == "listar":
                listado.listar()
            elif subcomando == "crear":
                codigo, marca, modelo, Kilometraje, precio = (
                    sys.argv[3],
                    sys.argv[4],
                    int(sys.argv[5]),
                    sys.argv[6],
                    float(sys.argv[7]),
                )
                listado.crear(codigo, marca, modelo, Kilometraje, precio)
            elif subcomando == "actualizar":
                codigo, nombre, existencia, proveedor, precio = (
                    sys.argv[3],
                    sys.argv[4],
                    int(sys.argv[5]),
                    sys.argv[6],
                    float(sys.argv[7]),
                )
                listado.actualizar(codigo, marca, modelo, Kilometraje, precio)
            elif subcomando == "editar_existencias":
                codigo, nueva_existencia = sys.argv[3], int(sys.argv[4])
               listado.editar_existencias(codigo, nueva_existencia)
            elif subcomando == "eliminar":
                codigo = sys.argv[3]
                listado.eliminar(codigo)
            else:
                print("Comando no valido para inventario.")
            listado.cerrar_conexion()

        elif sys.argv[1] == "--clientes":
            clientes = Clientes(config)

            subcomando = sys.argv[2]
            if subcomando == "listar":
                vehiculo.listar()
            elif subcomando == "crear":
                codigo, marca, precio = sys.argv[3], sys.argv[4], sys.argv[5]
                vehiculo.crear(codigo, marca, kilometraje)
            elif subcomando == "editar":
                codigo, marca, precio = sys.argv[3], sys.argv[4], sys.argv[5]
                vehiculo.editar(codigo, marca, kilometraje)
            elif subcomando == "eliminar":
                codigo = sys.argv[3]
                vehiculo.eliminar(codigo)
                
            reportes.cerrar_conexion()

        else:
            print("Comando no valido.")
    except psycopg2.Error as err:
        print("Error de conexion: {err}")
