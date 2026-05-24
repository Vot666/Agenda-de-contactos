contactos = {}
print("===Agenda de contactos===")
while True:
    print("1. Agregar contacto")
    print("2. Ver todos los contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    opcion = int(input("Seleccione una opción: "))
    match opcion:
        case 1:
            nombre = input("Nombre del contacto: ")
            if nombre in contactos:
                print("Este nombre ya esta agregado")
                continue
            telefono = int(input("Télefono: "))
            if telefono <= 0:
                print("Numero invalido")
                continue
            
            email = input("Email: ")
            contactos[nombre] = {"Telefono": telefono, "Email": email}

        case 2:
            if contactos == {}:
                print("Agenda vacia")

            else:
                for k, v in contactos.items():
                    print(f"Contacto: {k} | Telefono: {v['Telefono']} | Email: {v['Email']}")


        case 3:
            nombre = input("A quien desea buscar: ")
            if nombre in contactos:
                print(f"Nombre: {nombre} | Telefono: {contactos[nombre]['Telefono']} | Email: {contactos[nombre]['Email']}")

            else:
                print("Contacto no encontrado")

        case 4:
            nombre = input("Nombre del contacto a borrar: ")
            if nombre not in contactos:
                print("Contacto no encontado")

            else:
                del contactos[nombre]
                print(f"Se borro a {nombre} de la agenda")

        case 5:
            print("Saliendo de la agenda")
            break

        case _:
            print("Opcion invalida. Intente de nuevo")