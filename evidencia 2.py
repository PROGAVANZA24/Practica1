#Guardar numeros
def  guardarNumeros ():
    numerosGuardar  =  int ( input ( "¿Cuántos números vas a registrar ?:" ))
    listaNumeros  = []
    para  numero  en  rango ( numerosGuardar ):
        numeroGuardar  =  int ( input ( f'Ingrese el número a guardar (restan { numerosGuardar  -  numero } ): ' ))
        listaNumeros . añadir ( numeroGuardar )
    f  =  abierto ( "numeros.txt" , "w" )
    para  numero  en  listaNumeros :
        f . escribir ( f ' { numero } \ n ' )
    f . cerca
    print ( "Numeros registrados en el archivo." )
    print ( "Saliendo del sistema ..." )
    salir ()

#Bloque principal
seleccionUsuario  =  4
imprimir ( "*" * 60 )
@@ -11,7 +26,7 @@
    imprimir ( "*" * 60 )
    seleccionUsuario  =  int ( input ( "Ingrese una opción:" ))
    si  seleccionUsuario  ==  1 :
        aprobar
        guardarNumeros ()
    elif  seleccionUsuario  ==  2 :
        aprobar
    elif  seleccionUsuario  ==  3 :