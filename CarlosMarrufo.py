#Bloque principal
seleccionUsuario = 4
print("*"*60)
print(" "*28, "MENU")
print("*"*60)
while seleccionUsuario < 1 or seleccionUsuario > 3:
    print("¿Desea ingresar o buscar datos?")
    print("1. Ingresar datos")
    print("2. Buscar datos")
    print("3. Salir")
    print("*"*60)
    seleccionUsuario = int(input("Ingrese una opción: "))
    if seleccionUsuario == 1:
        pass
    elif seleccionUsuario == 2:
        pass
    elif seleccionUsuario == 3:
        print("Saliendo del sistema...")
        exit()
    else:
        print("Seleccione una opción valida (1-3).")
        print("*"*60)