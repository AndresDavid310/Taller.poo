import java.util.Scanner;

class Libro {
    String titulo;
    String autor;
    int año;
    boolean disponible = true;

    public Libro(String titulo, String autor, int año) {
        this.titulo = titulo;
        this.autor = autor;
        this.año = año;
    }

    public String prestar() {
        if (disponible) {
            disponible = false;
            return "El libro '" + titulo + "' ha sido prestado.";
        } else {
            return "El libro '" + titulo + "' no está disponible.";
        }
    }

    public String devolver() {
        disponible = true;
        return "El libro '" + titulo + "' ha sido devuelto.";
    }
}

class Usuario {
    String nombre;
    int id_usuario;

    public Usuario(String nombre, int id_usuario) {
        this.nombre = nombre;
        this.id_usuario = id_usuario;
    }

    public String tomarLibro(Libro libro) {
        return libro.prestar();
    }

    public String devolverLibro(Libro libro) {
        return libro.devolver();
    }
}

public class Biblioteca {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Crear usuario
        System.out.print("Ingrese el nombre del usuario: ");
        String nombre = sc.nextLine();
        System.out.print("Ingrese el ID del usuario: ");
        int id = sc.nextInt();
        sc.nextLine();
        Usuario usuario = new Usuario(nombre, id);

        // Crear libro
        System.out.print("Ingrese el título del libro: ");
        String titulo = sc.nextLine();
        System.out.print("Ingrese el autor: ");
        String autor = sc.nextLine();
        System.out.print("Ingrese el año: ");
        int anio = sc.nextInt();
        sc.nextLine();
        Libro libro = new Libro(titulo, autor, anio);

        int opcion;
        do {
            System.out.println("\n--- Biblioteca ---");
            System.out.println("1. Prestar libro");
            System.out.println("2. Devolver libro");
            System.out.println("3. Salir");
            System.out.print("Seleccione una opción: ");
            opcion = sc.nextInt();

            switch (opcion) {
                case 1:
                    System.out.println(usuario.tomarLibro(libro));
                    break;
                case 2:
                    System.out.println(usuario.devolverLibro(libro));
                    break;
                case 3:
                    System.out.println("Saliendo...");
                    break;
                default:
                    System.out.println("Opción inválida");
            }
        } while (opcion != 3);

        sc.close();
    }
}
