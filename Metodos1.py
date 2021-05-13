class Archivo:
    
    def __init__(self, lista_num = [1,2,3,4,5,6,7,8,9,10]):
        self.lista_num = lista_num

    #Metodo creador de archivos
    def archivo_txt(self):
        #Codigo para guardar una lista en un archivo
        f = open('C:\Archivos_Progra\Proyectos_Clonados\Practica1\ArchivoList.txt', 'w', encoding = 'utf8')
        for numero in self.lista_num:
            f.write(str(numero) + ' ')
        f.close

    #Metodo buscador de numeros en un archivo
    def buscador_num(self, x_numero):
        self.x_numero = str(x_numero)
        
        f = open('C:\Archivos_Progra\Proyectos_Clonados\Practica1\ArchivoList.txt')
        self.lista_temp = list(f.read())
        f.close
       
        if self.x_numero in self.lista_temp:
            print(f'El numero {self.x_numero} si se encuentra en el archivo')
        else:
            print(f'El numero {self.x_numero} no se encuentra en el archivo')