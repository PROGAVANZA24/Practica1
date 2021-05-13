class Archivo:
    
    def __init__(self, lista_num = [1,2,3,4,5,6,7,8,9,10]):
        self.lista_num = lista_num

    def archivo_txt(self):
        #Codigo para guardar una lista en un archivo
        f = open('C:\Archivos_Progra\Proyectos_Clonados\Practica1\ArchivoList.txt', 'w', encoding = 'utf8')
        for numero in self.lista_num:
            f.write(str(numero) + '\n')
        f.close