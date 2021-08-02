import random

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
L1 = [5, 0, 4, 2, 3, 1, 9, 8, 7, 6]

# for i in L1:
#     print(L1.index(i))
#     print(L.index(i))

def mutInsert(L, n):
    aux = 0
    aux1 = 0
    aux2 = 0

    if random.random() < 0.3:
        while n > 0:
            aux = random.randint(0, len(L)-1)
            aux1 = L[aux]
            L.pop(aux)
            aux2 = random.randint(0, len(L)-1)

            while aux2 == aux:
                aux2 = random.randint(0, len(L)-1)

            L.insert(aux2, aux1)

            print(L)
        
            n -= 1
        
        return L
    else:
        return L

def mutExchange(L):
    aux = 0
    aux1 = 0
    aux2 = 0
    aux3 = 0

    if random.random() < 0.3:
        aux = random.randint(0, len(L)-1)
        aux1 = L[aux]
        L.pop(aux)
        aux2 = random.randint(0, len(L)-1)

        while aux2 == aux:
            aux2 = random.randint(0, len(L)-1)
        
        aux3 = L[aux2]

        L.pop(aux2)
        L.insert(aux2, aux1)
        L.insert(aux, aux3)

        print('Esto es L en if')
        print(L)
        return L
    else:
        print('Esto es L en else')
        print(L)
        return L

#mutExchange(L)
# def listToString(s):
#     str1 = ''
#     for ele in s:
#         str1 += str(ele)

#     return str1

# def point(Li,Ls):
#     aux = []
#     aux1 = []
#     L = []
#     num = random.randint(1, len(Li)-1)

#     print(num)
#     print(Li)
#     print(Ls)

#     for i in range(num):
#         print(i)
#         aux.append(Li[i])
#         aux1.append(Ls[i])
    
#     Li.reverse()
#     Ls.reverse()
    
#     for i in range(num):
#         Li.pop()
#         Ls.pop()

#     print(aux)
#     print(aux1)

#     Li.reverse()
#     Ls.reverse()

#     for i in Li:
#         aux1.append(i)
    
#     for i in Ls:
#         aux.append(i)

#     print(aux)
#     print(aux1)

#     L.append(listToString(aux))
#     L.append(listToString(aux1))

#     return L

# print(point(L, L1))

# for i in range(0, len(L), 2):
#     print('Esto es el valor de i en L')
#     print(L[i])
#     print('Esto es el valor de i+1 en L')
#     print(L[i+1])
#     print('Esto es el valor de de L1[L[i]]')
#     print(L1[L[i]])
#     print('Esto es el valor de L1[L[i+1]]')
#     print(L1[L[i+1]])

# def tournament(L):
#     aux = 0
#     aux1 = 0

#     print('Esto es L')
#     print(L)
#     random.shuffle(L)
#     print('Esto es shuffle(L)')
#     print(L)
    
#     for _ in range(len(L)):
#         aux = random.choice(L)
#         aux1 = random.choice(L)
#         if  aux < aux1:
#             L2.append(aux1)
#         else:
#             L2.append(aux)
    
#     print('Esto es el resultado de tournament()')
#     return L2

# print(tournament(L))

# def sizeZero(n):
#     s = ''
#     while n > 0:
#         s += '0'
#         n -= 1
    
#     return s

# def int2Bin(L):
#     L1 = []
#     aux = 0
#     cad = ''

#     for i in L:
#         if aux < len(bin(i).split('0b')[1]):
#             print(aux)
#             aux = len(bin(i).split('0b')[1])
#         else:
#             print(aux)
    
#     for i in L:
#         cad = sizeZero(aux-len(bin(i).split('0b')[1])) + bin(i).split('0b')[1]
#         L1.append(cad)

#     return L1

# print('Esto es L')
# print(L)
# print('Esto es L Binaria')
# print(int2Bin(L))
# print(sizeZero(4))

#Roulette Algorithm
# counter = 0
# prob = 0

# for i in L:
#     counter += i

# print(counter)

# for i in L:
#     prob = i/counter
#     L1.append(prob)

# counter = 0

# for i in L1:
#     counter += i
#     L2.append(counter)

# counter = 0

# # for i in L2:
# #     counter += i

# print(L1)
# print(L2)
# #print(counter)

# L1.clear()
# ran = 0

# print('----------------------------------')

# tam = len(L)

# while len(L1) < tam:
#     ran = random.uniform(0, 1)
#     for i in L2:
#         if i < ran:
#             print(i)
#             print(ran)
#             print('--------------------------------------')
#             print()
#         else:
#             print(L2.index(i))
#             print()
#             L1.append(L[L2.index(i)])
#             L.pop(L2.index(i))
#             L2.remove(i)
#             print(ran)
#             print('--------------------------------------')

# print()
# print(L1)

#List Copy Method
# L = [1,2,3,4,5,6]
# L1 = L.copy()

# print('Esto es L')
# print(L)
# L.clear()

# print('La nueva L')
# print(L)
# print('Esto es L1')
# print(L1)