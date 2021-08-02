from random import randint
import math

class individuo:
    def __init__(self, i, funcion):
        self.j = bin(i).split('0b')
        self.alelo = self.j[1]
        self.apt = funcion
        #self.ind = [self.alelo, self.apt]
    
    def printGen(self):
        print('El gen es: ' + self.alelo)
    
    def printApt(self):
        print('La aptitud es: ' + str(self.apt))
    
    #def printInd(self):
     #   print(self.ind)

class aptitudes:
    def __init__(self, valor, fun):
        x = valor
        self.y = eval(fun)
        #print('y={}'.format(y))
        

class proba:
    def __init__(self, poblacion):
        self.indApt = [i.apt for i in poblacion]
        #print('Las aptitudes de cada individuo son: ')
        self.indApt.sort()
        print(self.indApt)
        self.sumApt = 0
        for i in self.indApt:
            self.sumApt += i
        print('Suma de aptitudes: ' + str(self.sumApt))
        self.prob = [round(i/self.sumApt, 2) for i in self.indApt]
        print('Probabilidades: ' + str(self.prob))
        self.sumProb = 0
        self.listSumProb = []
        for z in range(len(self.prob)):
            self.sumProb += self.prob[z]
            self.listSumProb.append(self.sumProb)
        print('Lista sumada de probabilidades: ')
        print(self.listSumProb)
        self.sumProb1 = 0
        for i in self.listSumProb:
            self.sumProb1 += i
        print('Suma total de todas las probabilidades: ' + str(self.sumProb1))

class seleccion:
    def __init__(self, q, cant, i, f, b):
        print('\tTipo de seleccion:\n1)Ruleta\n2)Torneo determinista\n3)Torneo probabilística')
        self.selec = int(input())
        self.cont = q-1

        self.aleatorios = [randint(i, f) for _ in range(cant)]
        self.aleatorios.sort()
        print(self.aleatorios)
        #self.aptAl = [aptitudes(k, self.b) for k in self.aleatorios]
        self.poblacion = [individuo(j, aptitudes(j, b).y) for j in self.aleatorios]

        for h in self.poblacion:
            h.printGen()
            h.printApt()
        self.prob = proba(self.poblacion)

        if(self.selec == 1):
            self.p = proba(self.poblacion)
            self.r = randint(0, int(self.p.sumProb1))
            print(self.r)
            self.list = self.p.listSumProb
            self.t = 0
            for z in range(len(self.list)):
                if(self.r < self.list[z]):
                    self.t = self.list[z]
                    #self.t1 = self.list[z+1]
            print('el padre 1 es: ' + str(self.t))
            #self.cruza = cruza()
        elif(self.selec == 2):
            self.p = proba(self.poblacion)
            self.list = self.p.indApt
            self.list.sort()
            self.aux1 = len(self.list)-1
            self.aux2 = len(self.list)-2
            self.t = self.list[self.aux1]
            self.t1 = self.list[self.aux2]
            print('El padre 1 es: ' + str(self.t))
            print('El padre 2 es: ' + str(self.t1))


class cruza:
    def __init__(self):
        print('\tTipo de Cruza:\n1)Un Punto\n2)N Puntos\n3)Uniforme')
        self.nCruza = int(input())

        if(self.nCruza == 1):
            self.muta = mutacion()

class mutacion:
    def __init__(self):
        print('\tTipo de Mutacion:\n1)Inserción\n2)Desplazamiento\n3)Intercambio')
        self.nMuta = int(input())

        if(self.nMuta == 1):
            self.select = seleccion()
            

class main():
    def __init__(self):
        print('Introduce la cantidad de generaciones')
        self.q = int(input())
        print('Introduce la cantidad de aleatorios')
        self.cant = int(input())
        print('Introduce el numero inicial del rango')
        self.i = int(input())
        print('Introduce el numero final del rango')
        self.f = int(input())
        print('Introduce la aptitud del individuo')
        self.b = str(input())

        self.s = seleccion(self.q, self.cant, self.i, self.f, self.b)


Iniciar = main()

#rand = [randint(0, 10) for _ in range(5)]
#pob = [individuo(j, aptitudes(j, 'x**2').y) for j in rand]
#prob = proba(pob)