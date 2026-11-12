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
        promedio = sum(est["notas"]) / len(est["notas"]) if est["notas"] else 0.0
        estado = "Aprobado" if promedio >= 11 else "Desaprobado"
        print(f"Código: {est['codigo']} | Nombre: {est['nombre']} | Carrera: {est['carrera']} | Promedio: {promedio:.2f} ({estado})")

def buscar_estudiante():
    print("\n--- Buscar Estudiante ---")
    codigo = input("Ingrese el código a buscar: ")
    for est in estudiantes:
        if est["codigo"] == codigo:
            print(f"Encontrado -> Nombre: {est['nombre']} | Carrera: {est['carrera']} | Notas: {est['notas']}")
            return
    print("No se encontró ningún estudiante con ese código.")

def registrar_nota():
    print("\n--- Registrar Nota ---")
    codigo = input("Ingrese el código del estudiante: ")
    for est in estudiantes:
        if est["codigo"] == codigo:
            try:
                nota = float(input("Ingrese la calificación (0 - 20): "))
                if 0 <= nota <= 20:
                    est["notas"].append(nota)
                    print("Nota registrada correctamente.")
                else:
                    print("La nota debe estar entre 0 y 20.")
            except ValueError:
                print("Error: debe ingresar un valor numérico.")
            return
    print("Estudiante no encontrado.")

def menu():
    while True:
        print("\n==========================================")
        print("   SISTEMA DE GESTIÓN DE ESTUDIANTES")
        print("==========================================")
        print("1. Registrar estudiante")
        print("2. Listar estudiantes y promedios")
        print("3. Buscar estudiante por código")
        print("4. Registrar nota")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            listar_estudiantes()
        elif opcion == "3":
            buscar_estudiante()
        elif opcion == "4":
            registrar_nota()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
    