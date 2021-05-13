def buscarNumeros():
    try:
        f = open("numeros.txt", "r")
        numeroEncontrado = 0
        numeroBuscar = int(input("Ingrese el número a buscar: "))
        for linea in f:
            if numeroBuscar == int(linea.rstrip()):
                numeroEncontrado = numeroEncontrado + 1
        if numeroEncontrado >= 1:
            print(f'El número se ha encontrado un total de {numeroEncontrado} veces en el archivo.')
        else:
            print("El número no se ha encontrado en el archivo.")
    except:
        crearArchivo = input("No se ha encontrado un archivo de datos, ¿quieres crear uno? (S/N): ").upper()
        while crearArchivo != "S" or crearArchivo != "N":
            if crearArchivo == "S":
                pass
            elif crearArchivo == "N":
                print("Saliendo del sistema...")
                exit()
            else:
                crearArchivo = input("Por favor ingresa una opción válida (S/N)").upper()

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
        buscarNumeros()
    elif seleccionUsuario == 2:
        pass
    elif seleccionUsuario == 3:
        print("Saliendo del sistema...")
    else:
        print("Seleccione una opción valida (1-3).")
        print("*"*60)