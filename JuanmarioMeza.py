class listadenumeros:
    def __init__(self, variable, montos, contador):
        self.variable=variable
        self.montos=montos
        self.contador=contador
        
def listanumeros(variable, montos, contador):
        variable = int(input(f'Introduce la cantidad de números a capturar{variable+1}: '))
        montos = list()

        contador=0
        while contador < variable:
            montos.append(input('Captura el número: '))
            contador = contador + 1
            print(montos)

   
    