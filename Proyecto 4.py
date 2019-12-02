import numpy as np
import random as r
from matplotlib import pyplot as plt
from matplotlib import style


def coordenadas(pos):
    '''
    Retorna las coordenadas del tablero para una posición del mismo
    '''
    sumador=0
    while True:
        if (pos + sumador) % 8 == 0:   # Como sé que para cualquier posición que tenga como coordenada x = 8 va a ser múltiplo de 8, voy sumando 1 a la posición hasta que
            x = 8-sumador              # se vuelva múltiplo de 8. Cuando esto se cumpla solo tengo que restar_ 1: La cantidad de veces que he sumado 1 a la posición y 2: El 8
            break                      # con eso tengo la coordenada en x
        sumador += 1
    if pos-x>0:
        y = (pos-x)//8+1
    else:
        y=1
    return [x,y]


def grados(column, row):
    '''
    Retorna los grados de libertad y sus posiciones en el tablero para unas coordenadas dadas
    '''
    Posicion = (column + 1) + row * 8  #Convierto la fila/columna en el número que corresponde

    column += 1
    row += 1#Conversión para trabajar más cómodo (de 1 a 8)
    Filas = {1: [1, 8], 2: [9, 16], 3: [17, 24], 4: [25, 32], 5: [33, 40], 6: [41, 48], 7: [49, 56], 8: [57, 64]} #Establezco de dónde a dónde van las respectivas filas
    Grados = 0
    posiciones=[]

    try:                                #Que intente restarle 1 a la fila, si no puede significa que por arriba no hay grados
        FilaActual = Filas[row - 1]     #En FilaActual ahora hay una lista con 2 números, el primero es el número más bajo de la fila y el segundo el más alto
    except:
        pass
    else:                               #Verifico que las 2 casillas a las que se puede mover el caballo que están 1 fila arriba de la posición estén disponibles
        if Posicion - 8 + 2 <= FilaActual[1]:
            Grados += 1
            posiciones.append(Posicion - 8 + 2)
        if Posicion - 8 - 2 >= FilaActual[0]:
            Grados += 1
            posiciones.append(Posicion - 8 - 2)
        try:                             # Como  se ha podido restar 1 a la fila, pruebo a ver si se puede restar 2, de poderse se ejecuta el mismo procedimiento para las casillas que están disponibles a 2 filas
            FilaActual = Filas[row - 2]
        except:
            pass
        else:
            if Posicion-16 + 1 <= FilaActual[1]:
                Grados += 1
                posiciones.append(Posicion-16 + 1)
            if Posicion-16 - 1 >= FilaActual[0]:
                Grados += 1
                posiciones.append(Posicion - 16 - 1)
    try:
        FilaActual = Filas[row+1]
    except:
        pass
    else:
        if Posicion + 8 + 2 <= FilaActual[1]:
            Grados += 1
            posiciones.append(Posicion + 8 + 2)

        if Posicion + 8 - 2 >= FilaActual[0]:
            Grados += 1
            posiciones.append(Posicion + 8 - 2)
        try:
            FilaActual = Filas[row+2]
        except:
            pass
        else:
            if Posicion + 16 + 1 <= FilaActual[1]:
                Grados += 1
                posiciones.append(Posicion + 16 + 1)
            if Posicion + 16 - 1 >= FilaActual[0]:
                Grados += 1
                posiciones.append(Posicion + 16 - 1)
    return Grados,posiciones



def Reiniciar(x,y):
    '''
    Retorna el tablero regenerado ( Con el 1 puesto en la posición inicial
    '''
    T = np.array([[ 1,  2,  3,  4,  5,  6,  7,  8],
                  [ 9, 10, 11, 12, 13, 14, 15, 16],
                  [17, 18, 19, 20, 21, 22, 23, 24],
                  [25, 26, 27, 28, 29, 30, 31, 32],
                  [33, 34, 35, 36, 37, 38, 39, 40],
                  [41, 42, 43, 44, 45, 46, 47, 48],
                  [49, 50, 51, 52, 53, 54, 55, 56],
                  [57, 58, 59, 60, 61, 62, 63, 64]])
    T[y, x] = 1
    return T


Tablero = np.array([[ 1,  2,  3,  4,  5,  6,  7,  8],
                    [ 9, 10, 11, 12, 13, 14, 15, 16],
                    [17, 18, 19, 20, 21, 22, 23, 24],
                    [25, 26, 27, 28, 29, 30, 31, 32],
                    [33, 34, 35, 36, 37, 38, 39, 40],
                    [41, 42, 43, 44, 45, 46, 47, 48],
                    [49, 50, 51, 52, 53, 54, 55, 56],
                    [57, 58, 59, 60, 61, 62, 63, 64]])

#    ***** Inicio aleatorio  ********

x = r.randint(0, 7)  # Columna
y = r.randint(0, 7)  # Fila
x = 0
y = 0
#Se hace una copia de la posición inicial para su posterior uso
Clonx = x
Clony = y

PosicionCaballo = 1

CasillasRecorridas=[[x,y]]

Tablero[y,x]=1                   # Marco la primera posición
while True:
    try:
        Grados, posiciones = grados(x, y) # Consigo los grados y las posiciones de ellos para la posición actual
        GradosLibertadSig=[] # Establezco una lista para almacenar los grados de libertad
        CoordenadasSig = []  # Lista para almacenar sus coordenadas
        for i in posiciones:        # Hallo la posición con menos grados
            Coordenadas = coordenadas(i)  #Tengo las coordenadas de la posición

            GradosLibertadSig.append(grados(Coordenadas[0]-1, Coordenadas[1]-1)[0]) # Hallo los grados de libertad para esas coordenadas y lo pongo en una lista
            CoordenadasSig.append(Coordenadas)

        PosicionCaballo += 1
        m = min(GradosLibertadSig)
        CasillasMax = [i for i, j in enumerate(GradosLibertadSig) if j == m]          #Lista de los ÍNDICES de las posiciones con menos grados de libertad
        Breaker=0
        #print(GradosLibertadSig,CoordenadasSig,len(CasillasMax),)

        while True:                         #While infinito para ir sacando las posiciones
            if len(CasillasMax)==1:            #Valor mínimo de
                breaker = 0
                Salir = False
                while True:
                    x = CoordenadasSig[CasillasMax[0]][0] - 1
                    y = CoordenadasSig[CasillasMax[0]][1] - 1
                    if not [x, y] in CasillasRecorridas:
                        print('a')
                        CasillasRecorridas.append([x, y])
                        Salir = True  # Variable que uso para posteriormente salir del while que contiene al while actual
                        break
                    else:  # Al entrar aquí también sigfnifica que la posición elegida ya ha sido ocupada previamente
                        breaker += 1
                    if breaker == 50:  # Como en este caso son varias posiciones, doy un margen de 50 para que los número aleatorios tengan la oportunidad de
                        breaker = 0  # acertar con alguna coordenada que no haya sido ocupada, de lo contrario elimino el conjunto de posiciones con menor grado de libertad
                        n = min(GradosLibertadSig)  # y sus respectivas coordenadas
                        for i in GradosLibertadSig:
                            try:
                                ABorrar = GradosLibertadSig.index(n)
                                GradosLibertadSig.remove(n)
                                CoordenadasSig.pop(ABorrar)
                            except:
                                break
                            else:
                                m = min(GradosLibertadSig)
                                CasillasMax = [i for i, j in enumerate(GradosLibertadSig) if j == m]
                if Salir:
                    break
            else:
                breaker = 0
                Salir = False
                while True:
                    RandomSquare = r.randint(0,len(CasillasMax)-1)
                    x = CoordenadasSig[CasillasMax[RandomSquare]][0]-1
                    y = CoordenadasSig[CasillasMax[RandomSquare]][1]-1
                    if not [x,y] in CasillasRecorridas:
                        print('a')
                        CasillasRecorridas.append([x,y])
                        Salir = True        #Variable que uso para posteriormente salir del while que contiene al while actual
                        break
                    else:                   #Al entrar aquí también sigfnifica que la posición elegida ya ha sido ocupada previamente
                        breaker += 1
                    if breaker == 50:                  #Como en este caso son varias posiciones, doy un margen de 50 para que los número aleatorios tengan la oportunidad de
                        breaker = 0                    #acertar con alguna coordenada que no haya sido ocupada, de lo contrario elimino el conjunto de posiciones con menor grado de libertad
                        n = min(GradosLibertadSig)     #y sus respectivas coordenadas
                        for i in GradosLibertadSig:
                            try:
                                ABorrar = GradosLibertadSig.index(n)
                                GradosLibertadSig.remove(n)
                                CoordenadasSig.pop(ABorrar)
                            except:
                                break
                            else:
                                m = min(GradosLibertadSig)
                                CasillasMax = [i for i, j in enumerate(GradosLibertadSig) if j == m]
                if Salir:
                    break
        Tablero[y, x] = PosicionCaballo         #Anoto la posición actual
        if PosicionCaballo == 64:
            break
    except:         #Reinicio del tablero ya que no llegó a ninguna solución
        pass
        x = Clonx
        y = Clony
        Tablero = Reiniciar(x,y)
        CasillasRecorridas = [[x, y]]
        PosicionCaballo = 1

#               ******          Armando el gráfico              ******

style.use("classic")
Relacion = {8: 1, 7: 2, 6: 3, 5: 4, 4: 5, 3: 6, 2: 7, 1: 8}
for i in range(0,len(CasillasRecorridas)):      #Le sumo 1 a todas las coordenadas y a la posición y la modifico para que comience a contar desde abajo
    CasillasRecorridas[i]= [CasillasRecorridas[i][0]+1,CasillasRecorridas[i][1]+1]
    CasillasRecorridas[i][1] = CasillasRecorridas[i][1] - (CasillasRecorridas[i][1] - Relacion[CasillasRecorridas[i][1]])
Primero = True
for i in CasillasRecorridas:
    try:
        PuntoSig = CasillasRecorridas.index(i) + 1
        x = i[0] + 0.5
        y = i[1] + 0.5
        xsig = CasillasRecorridas[PuntoSig][0]+0.5
        ysig = CasillasRecorridas[PuntoSig][1]+0.5
        if Primero:
            plt.plot(x,y,'b^')          #Para que se diferencia primera casilla
            Primero = False
        else:
            plt.plot(x,y,'ko')
        plt.plot([x,xsig],[y,ysig],'--r')
    except:
        plt.plot(CasillasRecorridas[63][0]+0.5,CasillasRecorridas[63][1]+0.5,'b^')          #Para que se diferencia última casilla (será igual que la primera, pero como el proceso inverso también funciona no importa)
        break
plt.grid()
plt.title("\nThe knight's tour\n")

print(Tablero)
plt.show()

