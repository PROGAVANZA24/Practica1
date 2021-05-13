lista= [5,10,15,20,25,30,35,40,45,50]
f=open("c:/EVIDENCIAS/Practica1/Numeros_lista.txt","w",encoding="utf8")
for num in lista:
    f.write(str(num)+'\n')
f.close

