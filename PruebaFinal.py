
usuarios = {}

def contar_caracteres(clave):
    return len(clave)

def contar_letras(clave):
    conta = 0
    for c in clave:
        if c.isalpha():
            conta +=1
    return conta

def contar_numeros(clave):
    conta = 0
    for c in clave:
        if c.isnumeric():
            conta +=1
    return conta
    
def agregar_usuario():
    while True:
        print("="*60)
        print("\t\t\tIngresar usuario\t\t")
        print("="*60)
        
        name = input("Ingrese el nombre del usuario: ").strip()
        
        if name in usuarios:
            print(f"El usuario {name} ya fue ingresado.")
        else:
            print("Usuario ingresado con exito")
                
            
            while True:
                genero = input("Ingrese el sexo del usuario, (M/F): ").upper()
                if genero != "M" and genero != "F":
                    print("Se debe ingresar M o F solamente, intente denuevo.")
                else:
                    break
            
            contra = ingresar_clave()

            usuarios[name] = {
                name: [contra,genero]
            }
            print("Usuario agregado con exito.")
            break


def validar_clave(clave):
    errores = []
    if contar_caracteres(clave) < 8:
        errores.append("la contraseña debe tener minimo 8 caracteres.")
    if contar_numeros(clave) < 1:
        errores.append("la contraseña debe tener minimo 1 numero")
    if contar_letras(clave) <1:
        errores.append("la contraseña debe tener como minimo 1 letra") 
    if errores:
        print("Contraseña inválida. Debe contener:")
        for e in errores:
            print(" -", e)
        return False
    return True


def ingresar_clave():
    while True:
        contrasena = input("Ingrese su contraseña: ")
        contrasena2 = input("Repita su contraseña: ")

        if contrasena != contrasena2:
            print("Las contraseñas no coinciden intentelo denuevo.")
            continue
        elif " " in contrasena:
            print("La contraseña no debe tener espacios.")
            continue
        elif not validar_clave(contrasena):
            continue
        return contrasena
    
def buscar_usuarios():
    if not usuarios:
        print("No hay usuarios registrados")
        return
    usuario = input("Ingrese el usuario a buscar: ")
    print("="*60)
    print("Mostrando usuario")
    print("="*60)

    print(f"los datos del usuario son: {dict(usuarios.values())}")
    
def borrar_usuario():
    name = input("Ingrese correo del usuario a eliminar: ").strip().lower()
    if name in usuarios:
        confirm = input(f"¿Seguro que quiere eliminar el usuario {name}? (s/n): ").strip().lower()
        if confirm == "s":
            del usuarios[name]
            print("Usuario eliminado.")
        else:
            print("Eliminación cancelada.")
    else:
        print("Usuario no encontrado.")

def menu():
    print("="*60)
    print("\t\t\tMENU PRINCIPAL")
    print("="*60)
    print("1-. Agregar usuario.")
    print("2-. Buscar usuario.")
    print("3-. eliminar usuario.")
    print("4.- salir")

    return input("Ingrese una opcion: ")

def main():
    while True:
        opcion = menu()

        match opcion:
            case "1":
                agregar_usuario()
            case "2":
                buscar_usuarios()
            case "3":
                borrar_usuario()
            case "4":
                print("Saliendo del programa.")
                break
            case _:
                print("porfavor ingrese una opcion valida")

main()
