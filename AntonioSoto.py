f=open("c:/Programas/Practica1/numeritos.txt","w",encoding="utf8")
def creararchivo(a):
    for numero in a:
        f.write(str(numero)+'\n')
