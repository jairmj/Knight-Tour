
import numpy as np
import random as r
from matplotlib import pyplot as plt
from matplotlib import style
from tkinter import *
from tkinter import messagebox as ms


root = Tk()

#Configuraciones de la ventana

root.geometry("800x350")
root.resizable(width=False, height= False)
root.iconbitmap(r'favicon.ico')
root.title("Knight's Tour")





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
    Posicion = (column + 1) + row * 8
    column += 1
    row += 1
    Filas = {1: [1, 8], 2: [9, 16], 3: [17, 24], 4: [25, 32], 5: [33, 40], 6: [41, 48], 7: [49, 56], 8: [57, 64]}
    Grados = 0
    posiciones=[]
    try:                                #Que intente restarle 1 a la fila, si no puede significa que por arriba no hay grados
        FilaActual = Filas[row - 1]
    except:
        pass
    else:                               #Verifico que las 2 posibles casillas que están 1 fila arriba de la posición estén dentro del rango de esa fila
        if Posicion - 8 + 2 <= FilaActual[1] and Posicion - 8 + 2 >= FilaActual[0]:
            Grados += 1
            posiciones.append(Posicion - 8 + 2)
        if Posicion - 8 - 2 >= FilaActual[0] and Posicion - 8 - 2 <= FilaActual[1]:
            Grados += 1
            posiciones.append(Posicion - 8 - 2)
        try:                             # Como  se ha podido restar 1 a la fila, pruebo a ver si se puede restar 2, de poderse se ejecuta el mismo procedimiento.
            FilaActual = Filas[row - 2]
        except:
            pass
        else:
            if Posicion - 16 + 1 >= FilaActual[0] and Posicion-16 + 1 <= FilaActual[1]:
                Grados += 1
                posiciones.append(Posicion-16 + 1)
            if Posicion - 16 - 1 <= FilaActual[1] and Posicion-16 - 1 >= FilaActual[0]:
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


Tablero = np.array([[1, 2, 3, 4, 5, 6, 7, 8],
                    [9, 10, 11, 12, 13, 14, 15, 16],
                    [17, 18, 19, 20, 21, 22, 23, 24],
                    [25, 26, 27, 28, 29, 30, 31, 32],
                    [33, 34, 35, 36, 37, 38, 39, 40],
                    [41, 42, 43, 44, 45, 46, 47, 48],
                    [49, 50, 51, 52, 53, 54, 55, 56],
                    [57, 58, 59, 60, 61, 62, 63, 64]])
TableroNuevo = np.array([[1, 2, 3, 4, 5, 6, 7, 8],
                    [9, 10, 11, 12, 13, 14, 15, 16],
                    [17, 18, 19, 20, 21, 22, 23, 24],
                    [25, 26, 27, 28, 29, 30, 31, 32],
                    [33, 34, 35, 36, 37, 38, 39, 40],
                    [41, 42, 43, 44, 45, 46, 47, 48],
                    [49, 50, 51, 52, 53, 54, 55, 56],
                    [57, 58, 59, 60, 61, 62, 63, 64]])
#    ***** Inicio aleatorio  ********


def ListaPosiciones(Tablero,Inx,Iny,rand,loop):
    if rand == 1:
        x = r.randint(0, 7)  # Columna
        y = r.randint(0, 7)  # Fila
    else:
        RelacionLis = {7: 1, 6: 2, 5: 3, 4: 4, 3: 5, 2: 6, 1: 7, 8:0}
        x = Inx - 1
        y = Iny - (Iny - RelacionLis[Iny])

    Clonx = x
    Clony = y

    PosicionCaballo = 1

    CasillasRecorridas=[[x,y]]
    intentos = 0
    Tablero[y,x]=1                   # Marco la primera posición
    while True:
        try:
            Grados, posiciones = grados(x, y) # Consigo los grados y las posiciones de ellos para la posición actual
            GradosLibertadSig=[] # Establezco una lista para almacenar los grados de libertad
            CoordenadasSig = []  # Lista para almacenar sus coordenadas
            for i in posiciones:        # Hallo la posición con más grados
                Coordenadas = coordenadas(i)  #Tengo las coordenadas de la posición

                GradosLibertadSig.append(grados(Coordenadas[0]-1, Coordenadas[1]-1)[0]) # Hallo los grados de libertad para esas coordenadas y lo pongo en una lista
                CoordenadasSig.append(Coordenadas)

            PosicionCaballo += 1
            m = min(GradosLibertadSig)
            CasillasMax = [i for i, j in enumerate(GradosLibertadSig) if j == m]          #Lista de índices de posiciones mínimas
            Breaker=0
            while True:                         #While infinito para ir sacando las posiciones
                if CasillasMax == 1:
                    x = CoordenadasSig[CasillasMax[0]][0]-1
                    y = CoordenadasSig[CasillasMax[0]][0]-1
                    if not [x,y] in CasillasRecorridas:
                        CasillasRecorridas.append([x,y])
                        break
                    else:                                               #Al entrar aquí significa que la posición con menor grado de libertad ya ha sido ocupada previamente,
                        Borro = GradosLibertadSig.index(CasillasMax[0]) #por lo que borro dicha posición con su respectiva coordenada
                        GradosLibertadSig.remove(CasillasMax[0])
                        CoordenadasSig.pop(Borro)
                        m = min(GradosLibertadSig)
                        CasillasMax = [i for i, j in enumerate(GradosLibertadSig) if j == m]
                else:
                    breaker = 0
                    Salir = False
                    while True:
                        RandomSquare = r.randint(0,len(CasillasMax)-1)
                        x = CoordenadasSig[CasillasMax[RandomSquare]][0]-1
                        y = CoordenadasSig[CasillasMax[RandomSquare]][1]-1
                        if not [x,y] in CasillasRecorridas:
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
            if loop == 0:
                if PosicionCaballo == 64:
                    print("Tablero (Arreglo de 8 x 8):\n")
                    print(Tablero, end=("\n\n"))
                    break
            elif loop == 1:
                if PosicionCaballo == 64:
                    GradLast,PosGradLast = grados(CasillasRecorridas[-1][0],CasillasRecorridas[-1][1])
                    PrimeraPosicion = TableroNuevo[CasillasRecorridas[0][1],CasillasRecorridas[0][0]]
                    if PrimeraPosicion in PosGradLast:
                        print("Tablero (Arreglo de 8 x 8):\n")
                        print(Tablero, end=("\n\n"))
                        break
                    elif not PrimeraPosicion in PosGradLast and intentos < 20:
                        intentos += 1
                        # Reinicio del tablero ya que no es cerrado
                        x = Clonx
                        y = Clony
                        Tablero = Reiniciar(x, y)
                        CasillasRecorridas = [[x, y]]
                        PosicionCaballo = 1
                    else:
                        return False
                        break

        except:         #Reinicio del tablero ya que no llegó a ninguna solución
            x = Clonx
            y = Clony
            Tablero = Reiniciar(x,y)
            CasillasRecorridas = [[x, y]]
            PosicionCaballo = 1
    return CasillasRecorridas


#               ******          Armando el gráfico              ******
def GraficaRecorrido(CasillasRecorridas,Tablero):
    if CasillasRecorridas == False:
        return ms.showinfo("Error","El programa no pudo encontrar un camino cerrado para las coordenadas establecidas.")
    else:
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
                    plt.plot(x,y,'bo')          #Para que se diferencia primera casilla
                    Primero = False
                else:
                    plt.plot(x,y,'ko')
                plt.plot([x,xsig],[y,ysig],'--r')
            except:
                plt.plot(CasillasRecorridas[63][0]+0.5,CasillasRecorridas[63][1]+0.5,'b^')          #Para que se diferencia última casilla (será igual que la primera, pero como el proceso inverso también funciona no importa)
                break
        plt.grid()
        plt.title("\nThe knight's tour\n")
        plt.show()

def Info():
    ms.showinfo("Información","'El recorrido del caballero' es un antiguo juego matemático en el que existen millones y millones de soluciones. Consiste en mover el caballo de ajedrez, con sus respectivas restricciones"
                              " (Movimiento en L), por todas las casillas del tablero únicamente colocándose una vez en cada una de ellas.")


def Curiosidad():
    ms.showinfo("Curiosidad","Si el caballo parte desde una esquina, no podrá realizar el recorrido de manera cerrada. Inténtalo!")


def Ayuda():
    ms.showinfo("Ayuda","Un recorrido cerrado es aquel en el que la posición inicial (Marcada con un círculo) y la posición final (Marcada con un triángulo) están conectadas mediante "
                        "un salto más del caballo en L. Cuando la posición final no se conecta en L con la inicial se llama recorrido abierto.")

def change(*args):
    pass

def PrintSetted():
    ms.showinfo("Alerta","EL gráfico del recorrido se abrirá en una ventana emergente o se imprimirá en el terminal")
    if Loopable.get() == 0:
        GraficaRecorrido(ListaPosiciones(Tablero,varX.get(),varY.get(),rand=0, loop = 0),Tablero)
    else:
        GraficaRecorrido(ListaPosiciones(Tablero, varX.get(), varY.get(), rand=0,loop = 1), Tablero)


def PrintRand():
    ms.showinfo("Alerta","EL gráfico del recorrido se abrirá en una ventana emergente o se imprimirá en el terminal")
    if Loopable.get() == 0:
        GraficaRecorrido(ListaPosiciones(Tablero,rand=1,Inx=0,Iny=0,loop=0),Tablero)
    else:
        GraficaRecorrido(ListaPosiciones(Tablero, rand=1, Inx=0, Iny=0, loop=1), Tablero)


# Menú superior

TopMenu = Menu(root)
root.config(menu= TopMenu)
Informacion = Menu(TopMenu, tearoff = 0)
TopMenu.add_cascade(label = "File", menu= Informacion)
Informacion.add_command(label = "Información", command = Info)
Informacion.add_command(label = "Ayuda", command = Ayuda)
Informacion.add_command(label = "Curiosidad", command = Curiosidad)
# Ayuda = Menu(TopMenu, tearoff = 0)
# Ayuda.add_command(label = "Información", command = Info)
# Curiosidad = Menu(TopMenu, tearoff = 0)
# Curiosidad.add_command(label = "Curiosidad", command = Curiosidad)




#                   ******           Opciones         ********


#                   ******           Coordenadas aleatorias        ********
RandomButton = Button(root, text="Coordenadas Aleatorias", command = PrintRand)
RandomButton.pack()
RandomButton.place(x=90, y=190)



#                   ******           Coordenadas establecidas        ********

Xoption = Label(root, text="X")
Xoption.pack()
Xoption.place(x=440, y=190)

Xoption = Label(root, text="Y")
Xoption.pack()
Xoption.place(x=530, y=190)


Options = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
]

varX = IntVar(root)
varX.set(Options[0])
varX.trace("w",change)

dropMenuX = OptionMenu(root, varX, Options[0], Options[1], Options[2], Options[3], Options[4], Options[5], Options[6], Options[7])
dropMenuX.pack()
dropMenuX.place(x=460, y=185)


varY = IntVar(root)
varY.set(Options[0])
varY.trace("w",change)

dropMenuY = OptionMenu(root, varY, Options[0], Options[1], Options[2], Options[3], Options[4], Options[5], Options[6], Options[7])
dropMenuY.pack()
dropMenuY.place(x=550, y=185)


StartButton = Button(root,text = "Enviar coordenadas", command=PrintSetted)
StartButton.pack()
StartButton.place(x = 620, y = 187)

#     **********     Forzar Recorrido Cerrado     ********


Loopable = IntVar()
CheckLoopSetted = Checkbutton(root, text="Forzar un camino cerrado", variable=Loopable)
CheckLoopSetted.pack()
CheckLoopSetted.place(x=250, y=250)


#        *************         Encabezado        ***************


title = PhotoImage(file = "titulo.png")
Ltitle = Label(root, image = title)
Ltitle.pack()
Ltitle.place(x = 130, y = 30)


root.mainloop()