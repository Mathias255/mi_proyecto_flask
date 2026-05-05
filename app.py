from flask import Flask
from modelos.entidades import Autor, Categoria, Libro
from libros.gestion import Inventario, Usuario

app = Flask(__name__)

@app.route('/')
def index():

    autor1 = Autor("Gabriel García Márquez", "Colombiano", "6 de marzo de 1927", ["Premio Nobel de Literatura"], "Cien años de soledad, El amor en los tiempos del cólera")

    cat1 = Categoria("Novela", "Obras de ficción narrativa", "Pasillo 1", False, "CAT001")

    libro1 = Libro("Cien años de soledad", autor1, cat1, "Editorial Sudamericana", "1967", 20.99, "ISBN1234567890")

    mi_tienda = Inventario("Libreria Central", "Juan Perez", "2024-05-01", 100, "Bogotá")
    mi_tienda.agregar_libro(libro1, 10)

    cliente1 = Usuario("Lector_pro", "maria@example.com", "Oro", 100, True)

    return f"""
    <h1>Sistema de Librería Activo</h1>
    <p><b>Libro:</b> {libro1.titulo}</p>
    <p><b>Autor:</b> {libro1.autor.nombre}</p>
    <p><b>Ubicación:</b> {libro1.categoria.pasillo}</p>
    <p><b>Cliente:</b> {cliente1.nickname} (Nivel: {cliente1.nivel})</p>
    """

if __name__ == "__main__":
    app.run(debug=True)