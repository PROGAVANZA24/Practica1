archivo=open('Numeros_lista.txt','r')
'''archivo=str()'''
'''print (archivo.read())'''
num=input('Numero que desea encontrar: ')
for linea in archivo:
    if num in linea:
        print('Numero encontrado')
    else:
        print('No encontrado')
       