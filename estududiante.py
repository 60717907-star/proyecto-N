estudiantes = []

def agregar_estudiante():
    print("\n--- Registrar Nuevo Estudiante ---")
    codigo = input("Ingrese el código del estudiante: ")
    nombre = input("Ingrese el nombre completo: ")
    carrera = input("Ingrese la carrera profesional: ")
    
    estudiante = {
        "codigo": codigo,
        "nombre": nombre,
        "carrera": carrera,
        "notas": []
    }
    estudiantes.append(estudiante)
    print(f"Estudiante {nombre} registrado con éxito.")

def listar_estudiantes():
    print("\n--- Lista de Estudiantes Registrados ---")
    if not estudiantes:
        print("No hay estudiantes registrados todavía.")
        return
    
    for est in estudiantes:
        print(f"Código: {est['codigo']} | Nombre: {est['nombre']} | Carrera: {est['carrera']}")

def menu():
    while True:
        print("\n==========================================")
        print("   SISTEMA DE GESTIÓN DE ESTUDIANTES")
        print("==========================================")
        print("1. Registrar estudiante")
        print("2. Listar estudiantes")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            listar_estudiantes()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()