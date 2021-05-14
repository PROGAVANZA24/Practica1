f=open("c:/Programas/Practica1/numeritos.txt","w",encoding="utf8")
def creararchivo(a):
    for numero in a:
        f.write(str(numero)+'\n')
def buscar(e):
    contador = 0
    for numero in e:
        if numero ==1:
            contador = contador+1
    print ("El número 1 se encuentra ", contador, "veces.")

i = int(input('Hola usuario, selecciona la cantidad de numeros a capturar: '))
lista = list(range(i))
for e in lista:
    lista1 = int(input(f'Selecciona el total número {e+1}: '))
    lista[e] = lista1


creararchivo(lista)
buscar(lista)
        
f.close

print ('programa terminado')
#Olvide tomar foto del segundo metodo