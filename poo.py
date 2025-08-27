class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f"El libro '{self.titulo}' ha sido prestado."
        else:
            return f"El libro '{self.titulo}' no está disponible."

    def devolver(self):
        self.disponible = True
        return f"El libro '{self.titulo}' ha sido devuelto."


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def tomar_libro(self, libro):
        resultado = libro.prestar()
        if "prestado" in resultado:
            self.libros_prestados.append(libro)
        return resultado

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
            return libro.devolver()
        return f"{self.nombre} no tiene el libro '{libro.titulo}'."


# -----------------------------
# Programa principal con entradas
# -----------------------------

# Crear usuario
nombre_usuario = input("Ingrese el nombre del usuario: ")
id_usuario = int(input("Ingrese el ID del usuario: "))
usuario = Usuario(nombre_usuario, id_usuario)

# Crear libro
titulo = input("Ingrese el título del libro: ")
autor = input("Ingrese el autor: ")
anio = int(input("Ingrese el año: "))
libro = Libro(titulo, autor, anio)

# Menú
while True:
    print("\n--- Biblioteca ---")
    print("1. Prestar libro")
    print("2. Devolver libro")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print(usuario.tomar_libro(libro))
    elif opcion == "2":
        print(usuario.devolver_libro(libro))
    elif opcion == "3":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida")
