# Clase Libro
class Libro:
    def __init__(self, titulo, autor, año , disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.disponible = disponible

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        else:
            return False

    def devolver(self):
        self.disponible = True


# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def tomar_libro(self, libro):
        if libro.prestar():
            self.libros_prestados.append(libro)
            print(f"{self.nombre} ha tomado el libro '{libro.titulo}'.")
        else:
            print(f"El libro '{libro.titulo}' no está disponible.")

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro)
            print(f"{self.nombre} ha devuelto el libro '{libro.titulo}'.")
        else:
            print(f"{self.nombre} no tiene el libro '{libro.titulo}'.")


# Clase Biblioteca
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.usuarios = []

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuario '{usuario.nombre}' registrado en la biblioteca.")

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None


# ---------------- Ejemplo de uso ----------------
if __name__ == "__main__":
    # Crear biblioteca
    biblio = Biblioteca("Biblioteca Central")

    # Crear libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605)

    # Agregar libros a la biblioteca
    biblio.agregar_libro(libro1)
    biblio.agregar_libro(libro2)

    # Crear usuarios
    usuario1 = Usuario("Ana", 101)
    usuario2 = Usuario("Carlos", 102)

    # Registrar usuarios
    biblio.registrar_usuario(usuario1)
    biblio.registrar_usuario(usuario2)

    # Préstamos y devoluciones
    usuario1.tomar_libro(libro1)
    usuario2.tomar_libro(libro1)  # No podrá porque ya está prestado
    usuario1.devolver_libro(libro1)
    usuario2.tomar_libro(libro1)  # Ahora sí podrá tomarlo
