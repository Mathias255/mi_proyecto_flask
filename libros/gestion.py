from modelos.entidades import Libro

class Inventario:
    def __init__(self, sucursal, encargos, ultima_version, capacidad, cuidad):
        self.lista_libros = []
        self.sucursal = sucursal
        self.encargos = encargos
        self.ultima_version = ultima_version
        self.capacidad = capacidad
        self.cuidad = cuidad

    def agregar_libro(self, libro_objeto, cantidad):
        self.lista_libros.append({"libro": libro_objeto, "stock": cantidad})
        print(f"->{libro_objeto.titulo} añadido al inventario de {self.sucursal}")

class Usuario:
    def __init__(self, nickname, nombre, email, nivel, puntos, esta_activo):
        self.nickname = nickname
        self.nombre = nombre
        self.email = email
        self.nivel = nivel
        self.puntos = puntos
        self.esta_activo = esta_activo  

        