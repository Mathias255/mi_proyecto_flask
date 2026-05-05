class Autor:
    def __init__(self, nombre, nacionalidad, fecha_nacimiento, premios, bibliografia):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.premios = premios
        self.bibliografia = bibliografia

class Categoria:
    def __init__(self, nombre, descripcion, pasillo, es_adulto, codigo):
        self.nombre = nombre
        self.descripcion = descripcion
        self.pasillo = pasillo
        self.es_adulto = es_adulto
        self.codigo = codigo

class Libro:
    def __init__(self, titulo, autor, categoria, editorial, fecha_publicacion, precio, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.editorial = editorial
        self.fecha_publicacion = fecha_publicacion
        self.precio = precio
        self.isbn = isbn