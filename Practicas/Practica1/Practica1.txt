import random
import math
import matplotlib.pyplot as plt

#Aqui se defienen las funciones utilizando la libreria math
def funcion1(num):
    return num**2

def funcion2(num):
    return abs((num-5)/(2+math.sin(num)))

def funcion3(num):
    return ((math.exp(num) - math.exp(-num)))

# Función Generar Población
# param
#   num_poblacion: representa la cantidad de individuos que se crearan en la primera generación.
#   num_alelos: representa la cantidad de alelos que contendrá un cromosoma.
#   opc: representa la opción para elegir la función para evaluar la aptitud de cada individuo.
def Generar_poblacion(num_poblacion,num_alelos,opc):


    cromosoma = []
    arreglo_bin = []
    poblacion = []

    # Aasignamos un número aleatorio para después comparar:
    #   si es mayor a 0.5, agregamos un 1 al cromosoma.
    #   si es menor, agregamos un 0.
    # Hasta completar la cantidad de población solicitada.     
    for i in  range(1,(num_poblacion*num_alelos)+1):
        
        if i%num_alelos == 0:

            if random.random() > 0.5:
                cromosoma.append(1)
            else:
                cromosoma.append(0)
            
            arreglo_bin.append(cromosoma)
            cromosoma = []
        else:
            if random.random() > 0.5:
                cromosoma.append(1)
            else:
                cromosoma.append(0)
        
    print(len(arreglo_bin))
    print(arreglo_bin)   

   
    # Convertimos cada cromosoma a un valor real 
    # y cada individuo lo evaluamos en la función de aptitud elegida.    
        
    for i in range(len(arreglo_bin)):

        str_bin = ""

        str_bin = "".join( map(str,arreglo_bin[i]) )

        if opc == 1:
            poblacion.append(funcion1(int(str_bin,2)))
        elif opc == 2:
            poblacion.append(funcion2(int(str_bin,2)))
        elif opc == 3:
            poblacion.append(funcion3(int(str_bin,2)))  
    


    # Graficación de la aptitud de cada individuo.    
    
    arreglo_x = [i for i in range(1,num_poblacion+1)]

    print(len(poblacion))
    print(poblacion)

    plt.plot(arreglo_x, poblacion)
    plt.show()
         



#Sección del "main"
if __name__ == "__main__":

#Aqui se le pide al usuario que ingrese con un numero, la función con la que se va evaluar los individuos
    opc = int(input('''

            Selecciona la función (escribe número).

            1. f(x) = x^2
            2. f(X) = |(x-5)/2+sin(x)|
            3. f(x) = (e^x - e^-x) 
    '''))
#Aqui de le pide al usuario el tamaño de la población, el numero de generaciones que habra y el tamaño de los alelos
    num_poblacion =  int(input("Ponga el numero de la Población \n"))
    num_generacion =  int(input("Ponga el numero de Generaciones \n"))
    num_alelos =  int(input("Ponga el tamaño de alelos \n"))

#Aqui se le manda los datos al la funcion "Generar_poblacion"    
    for i in range(num_generacion):
        
        Generar_poblacion(num_poblacion,num_alelos,opc)
     

    


