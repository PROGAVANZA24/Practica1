lista = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#Codigo para crear un archivo .txt
f = open('C:\Archivos_Progra\Proyectos_Clonados\Practica1\ArchivoLista.txt', 'w', encoding = 'utf8')
#Codigo para ingresar la lista de numeros en el archivo .txt creado
for numero in lista:
    f.write(str(numero) + '\n' )
f.close
