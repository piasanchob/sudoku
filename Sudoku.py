# importa tkinter y otros modulos

import random

from tkinter import *

import time

import threading

import pickle

from pickle import dump

import os

import numpy

import webbrowser as wb

from tkinter import messagebox

import winsound

from winsound import *

import pygame

#pone musicona

pygame.init()
pygame.mixer.pre_init(44100,16,2,4096)

#size = (width, height)

pygame.mixer.music.load("deku.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)


#globaliza y define tiempo para usar en el timer

global tiempo

global textoTiempo

global perdio

tiempo = 0

textoTiempo = ""

#mejorjugador = True

perdio = False

facil1 = [[0,0,0,2,6,0,7,0,1],
          [6,8,0,0,7,0,0,9,0],
          [1,9,0,0,0,4,5,0,0],
          [8,2,0,1,0,0,0,4,0],
          [0,0,4,6,0,2,9,0,0],
          [0,5,0,0,0,3,0,2,8],
          [0,0,9,3,0,0,0,7,4],
          [0,4,0,0,5,0,0,3,6],
          [7,0,3,0,1,8,0,0,0]]


facil2 = [[2,0,0,3,0,0,0,0,0],
          [8,0,4,0,6,2,0,0,3],
          [0,1,3,8,0,0,2,0,0],
          [0,0,0,0,2,0,3,9,0],
          [5,0,7,0,0,0,6,2,1],
          [0,3,2,0,0,6,0,0,0],
          [0,3,2,5,9,6,4,8,7],
          [0,2,0,0,0,9,1,4,0],
          [6,0,1,2,5,0,8,0,9],
          [0,0,0,0,0,1,0,0,2]]

facil3 = [[0,0,0,3,9,0,0,1,0],
          [5,0,1,0,0,0,0,4,0],
          [9,0,0,7,0,0,5,0,0],
          [6,0,2,5,3,0,0,7,0],
          [0,0,0,0,7,0,0,0,8],
          [7,0,0,8,0,0,9,0,3],
          [8,0,3,0,1,0,0,9,0],
          [0,9,0,2,0,6,0,0,7],
          [4,0,0,0,0,3,0,6,1]]
          
         

solucionfacil1 = [[4,3,5,2,6,9,7,8,1],
                  [6,8,2,5,7,1,4,9,3],
                  [1,9,7,8,3,4,5,6,2],
                  [8,2,6,1,9,5,3,4,7],
                  [3,7,4,6,8,2,9,1,5],
                  [9,5,1,7,4,3,6,2,8],
                  [5,1,9,3,2,6,8,7,4],
                  [2,4,8,9,5,7,1,3,6],
                  [7,6,3,4,1,8,2,5,9]]

solucionfacil2 = [[2,7,6,3,1,4,9,5,8],
                  [8,5,4,9,6,2,7,1,3],
                  [9,1,3,8,7,5,2,6,4],
                  [4,6,8,1,2,7,3,9,5],
                  [5,9,7,4,3,8,6,2,1],
                  [1,3,2,5,9,6,4,8,7],
                  [3,2,5,7,8,9,1,4,6],
                  [6,4,1,2,5,3,8,7,9],
                  [7,8,9,6,4,1,5,3,2]]

solucionfacil3 = [[2,4,8,3,9,5,7,1,6],
                  [5,7,1,6,2,8,3,4,9],
                  [9,3,6,7,4,1,5,8,2],
                  [6,8,2,5,3,9,1,7,4],
                  [3,5,9,1,7,4,6,2,8],
                  [7,1,4,8,6,2,9,5,3],
                  [8,6,3,4,1,7,2,9,5],
                  [1,9,5,2,8,6,4,3,7],
                  [4,2,7,9,5,3,8,6,1]]
          

medio1 = [[0,0,0,8,3,2,0,9,0],
          [0,0,0,0,0,5,7,0,6],
          [1,0,0,6,0,0,0,0,0],
          [3,0,0,0,0,0,0,0,0],
          [6,7,4,0,0,0,8,5,1],
          [0,0,0,0,0,0,0,0,7],
          [0,0,0,0,0,1,0,0,5],
          [9,0,2,5,0,0,0,0,0],
          [0,3,0,2,7,6,0,0,0]]

solucionmedio1 = [[7,5,6,8,3,2,1,9,4],
                  [2,9,3,4,1,5,7,8,6],
                  [1,4,8,6,9,7,5,2,3],
                  [3,8,1,7,5,4,9,6,2],
                  [6,7,4,3,2,9,8,5,1],
                  [5,2,9,1,6,8,3,4,7],
                  [4,6,7,9,8,1,2,3,5],
                  [9,1,2,5,4,3,6,7,8],
                  [8,3,5,2,7,6,4,1,9]]

medio2 = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

solucionmedio2 = [[5,3,4,6,7,8,9,1,2],
                  [6,7,2,1,9,5,3,4,8],
                  [1,9,8,3,4,2,5,6,7],
                  [8,5,9,7,6,1,4,2,3],
                  [4,2,6,8,5,3,7,9,1],
                  [7,1,3,9,2,4,8,5,6],
                  [9,6,1,5,3,7,2,8,4],
                  [2,8,7,4,1,9,6,3,5],
                  [3,4,5,2,8,6,1,7,9]]

medio3 = [[5,0,9,0,0,0,0,0,7],
          [0,8,0,0,1,0,5,2,0],
          [0,0,3,0,8,4,0,0,1],
          [0,9,0,7,0,0,0,0,2],
          [4,0,0,0,5,0,3,9,0],
          [8,0,2,1,0,0,0,0,4],
          [0,0,0,3,0,2,0,0,5],
          [0,4,0,0,0,0,7,0,0],
          [1,0,7,0,9,0,0,8,0]]

solucionmedio3 = [[5,1,9,6,2,3,8,4,7],
                  [6,8,4,9,1,7,5,2,3],
                  [7,2,3,5,8,4,9,6,1],
                  [3,9,6,7,4,8,1,5,2],
                  [4,7,1,2,5,6,3,9,8],
                  [8,5,2,1,3,9,6,7,4],
                  [9,6,8,3,7,2,4,1,5],
                  [2,4,5,8,6,1,7,3,9],
                  [1,3,7,4,9,5,2,8,6]]

dif =  [[2,0,0,0,0,1,4,0,0],
        [7,0,0,0,9,0,0,0,0],
        [0,3,0,0,5,6,0,0,2],
        [0,7,0,2,1,8,5,0,6],
        [1,0,2,0,0,5,9,3,0],
        [6,0,0,0,8,0,0,0,0],
        [9,0,0,5,0,3,8,0,0],
        [4,1,8,0,2,0,0,6,5]]

soluciondificil1 = [[2,9,6,8,7,1,4,5,3],
                   [7,4,5,3,9,2,6,8,1],
                   [8,3,1,4,5,6,7,9,2],
                   [3,7,9,2,1,8,5,4,6],
                   [1,8,2,6,4,5,9,3,7],
                   [5,6,4,7,3,9,1,2,8],
                   [6,5,3,1,8,4,2,7,9],
                   [9,2,7,5,6,3,8,1,4],
                   [4,1,8,9,2,7,3,6,5]]

dificil2 = [[0,0,0,0,0,0,2,0,0],
            [0,8,0,0,0,7,0,9,0],
            [6,0,2,0,0,0,5,0,0],
            [0,7,0,0,6,0,0,0,0],
            [0,0,0,9,0,1,0,0,0],
            [0,0,0,0,2,0,0,4,0],
            [0,0,5,0,0,0,6,0,3],
            [0,9,0,4,0,0,0,7,0],
            [0,0,6,0,0,0,0,0,0]]

soluciondificil2 = [[9,5,7,6,1,3,2,8,4],
                    [4,8,3,2,5,7,1,9,6],
                    [6,1,2,8,4,9,5,3,7],
                    [1,7,8,3,6,4,9,5,2],
                    [5,2,4,9,7,1,3,6,8],
                    [3,6,9,5,2,8,7,4,1],
                    [8,4,5,7,9,2,6,1,3],
                    [2,9,1,4,3,6,8,7,5],
                    [7,3,6,1,8,5,4,2,9]]

dificil3 = [[7,0,0,0,0,8,0,0,1],
            [0,1,0,0,0,0,0,3,0],
            [0,0,0,1,5,0,0,0,9],
            [0,0,0,0,6,0,0,0,7],
            [2,0,0,0,1,0,0,0,0],
            [5,0,0,0,0,0,1,2,6],
            [3,6,8,0,0,0,0,0,0],
            [0,2,0,0,0,0,0,1,0],
            [1,0,0,8,0,0,0,0,4]]



# funcion timer

def timer(seg, label):
    label.config(text=seg)
    if (seg == 20):
        return perder(True)
    else:
        time.sleep(1)
        return timer(seg - 1)


def reloj(seg, label):
    label.config(text=seg)
    if (seg == 20):
        return perder(True)
    else:
        time.sleep(1)
        return timer(seg - 1)


# dimensiones para la matriz

row = 9

column = 9

# variables globales para el timer y verificar si puede seguir

puedeseguir = True
conTimer = True
conReloj = False

# numero mayor es el numero que tiene que llegar a ser 2048 para ganar

#numeromayor = 0

# si la persona escoge que quiere timer lo despliega

def sitimerreloj():
    global ventana_principal

    print("hola")
    conta = Label(ventana_principal).place(x=100, y=450)
    if conTimer:
        threading.Thread(target=timer, args=[20, conta]).start()  # si es timer 600
    if conReloj:
        threading.Thread(target=reloj, args=[20, conta]).start()  # si es reloj 0 
    else:
        print("Ok mongolito")


# crea ventana donde se va a jugar

def crearVentana():
    
    global ventana_principal

    ventana_principal = Tk()

    ventanaJuego()

# configura las dimensiones de la ventana del juego

def crearVentanaConfig():
    global configwindow
    configwindow = Tk()
    ventanaConfig()
    configwindow.geometry("500x500")

def devolverAInt(p):
    lista = p.split(":")
    horas = int(lista[0]) * 3600
    minutos = int(lista[1]) * 60
    seg = int(lista[2])
    return horas + minutos + seg
#acomoda a 
def bubbleSort():
    global a
    n = len(a) 
  
    
    for i in range(n): 
  
        
        for j in range(0, n-i-1): 
  
            elemento1 = devolverAInt(a[j][1])
            elemento2 = devolverAInt(a[j+1][1])
            if elemento1 > elemento2: 
                a[j], a[j+1] = a[j+1], a[j]
# imprime el nombre insertado del jugador en un entry y el tiempo que duró
def imprimir(entry):
    global content, a
    content = entry.get()
    a.append((content,textoTiempo))
    bubbleSort()
    a.reverse()
   
    top()
    
a = [] #liata para el top 10

def windowtop10(): #inserta en el top 10
    
    global top10
    top10 = Tk()
    top10.geometry("500x500")
    top10.config(bg = "yellow")
    pos = 0
    lstplayers = Listbox(top10,width = 50)
    for entry in a:
        #a.sort(reverse = True)
        lstplayers.insert(pos, entry)
        pos += 1
        
    
    
    lstplayers.place(x = 100, y = 120)

    
                                                                                                                          
    top10.mainloop()

def sacarBest():
    
    num = (a[0])

    return num

 #guarda la partida el nombre y el timer para jugar despues
 #guarda top 10
def lista10():
    archivo = open("mejoresjugadores.txt","w+")
    archivo.write(str(matrix))
    archivo.close()

def top():
    archivo = open("top10.txt","w+")
    archivo.write(str(a))
    archivo.close()
    


# boton del mejor jugador

"""def mejorjugador1():
    tp = Tk()
    tp.geometry("500x500")
    messagebox.showinfo(message = sacarBest(),title = "Mejor jugador")"""
    
    


def leer (archivo):

    resultado = ""

    if(os.path.exists(archivo)):

        fo = open(archivo, "w+") # abre en forma

        # de solo lectura

        resultado = fo.read()

        fo.close()

    #retorna lo que leyo del archivo

    return resultado

def cargarArchivo():
    global matrix
    f = open("mejoresjugadores.txt", "r")
    #ventana_principal.after(1000, timeL, label)
    matrix = eval(f.read())
    print(matrix)
    f.close()
    crearVentana()
    moverMatriz(ventana_principal,matrix)

def cargarArchivo2():
    global a
    try:
        x = open("top10.txt", "r")
        a = eval(x.read())
        #textoTiempo = eval(x.read())
        #print(textoTiempo)
        x.close()
        #moverMatriz(ventana_principal,matrix)
    except:
        a = []

    
    
# si la opcion es 2, "CONFIGURAR" abre otra ventana

def config():
    pass

# se despliega el manual de usuario

def ayuda():
    wb.open_new(r"C:\Users\user\Documents\programacion William\progra\programa1_piasancho\manual_de_usuario_2048.pdf")

    
       
    
#acerca de despliega un messagebox con la info del programa
    
def acercade():
    
    acercaDe = Tk()

    messagebox.showinfo("Acerca de",("Nombre de la aplicación: Juego Sudoku",
                        "Versión: 1.0",
                        "Fecha de creación: Noviembre 2019",
                        "Autor: Pía Sancho Zamora",
                        "Tecnólogico de Costa Rica"))
    
#si quiere salir sale del programa
    
def salir():
    exit(0)

#ventana del menu
    
def window():
    window = Tk()

    window.geometry("500x500")

    # titulo de la ventana

    window.title("2048")

    # Titulo del juego

    titulo = Label(window, text="2048 GAME")

    window.config(bg="SeaGreen1")

    #botones del menu
    
    prueba = Radiobutton(window,
                         text="JUGAR",
                         indicatoron=0,
                         width=20,
                         padx=20,
                         variable=1,
                         command=crearVentana,
                         value=1)
    prueba2 = Radiobutton(window,
                          text="CONFIGURAR",
                          indicatoron=0,
                          width=20,
                          padx=20,
                          variable=2,
                          command=crearVentanaConfig,
                          value=2)

    prueba3 = Radiobutton(window,
                          text="AYUDA",
                          indicatoron=0,
                          width=20,
                          padx=20,
                          variable=3,
                          command=ayuda,
                          value=3)
    
    prueba4 = Radiobutton(window,
                          text="ACERCA DE",
                          indicatoron=0,
                          width=20,
                          padx=20,
                          variable=4,
                          command=acercade,
                          value=4)
    prueba5 = Radiobutton(window,
                          text="SALIR",
                          indicatoron=0,
                          width=20,
                          padx=20,
                          variable=5,
                          command=salir,
                          value=5)

    prueba6 = Radiobutton(window,
                          text="CARGAR PARTIDA",
                          indicatoron=0,
                          width=20,
                          padx=20,
                          variable=6,
                          command=lambda: window.after(200, cargarArchivo()),
                          value=6)
    prueba7 = Radiobutton(window,
                          text="PARTIDAS",
                          indicatoron=0,
                          width=20,
                          padx=20,
                          variable=3,
                          command=None,
                          value=3)
    
    prueba.pack()
    prueba2.pack()
    prueba3.pack()
    prueba4.pack()
    prueba5.pack()
    prueba6.pack()
    prueba7.pack()
    #matrix = crearMatrix()
    cargarArchivo2()
    window.mainloop()

#calcula el numero mayor
    
"""def calcularMayor():
    maximo = 0
    for lista in matrix:
        for elem in lista:
            if elem > maximo:
                maximo = elem
    return maximo"""


# crea matriz

def crearMatrixfacil():
    diccfacil = {1:facil1,2:facil2,3:facil3}
    global matrix
    matrix = diccfacil[random.randint(1,3)]
    if matrix == facil1:
        solucion = solucionfacil1
    if matrix == facil2:
        solucion = solucionfacil2
    else:
        solucion = solucionfacil3
def crearMatrixmedio():
    diccmedio = {1:medio1,2:medio2,3:medio3}
    global matrix
    matrix = diccmedio[random.randint(1,3)]
    if matrix == medio1:
        solucion = solucionmedio1
    if matrix == medio2:
        solucion = solucionmedio2
    else:
        solucion = solucionmedio3
def crearMatrixdificil():
    diccdificil = {1:dif,2:dificil2,3:dificil3}
    
    global matrix
    matrix = diccdificil[random.randint(1,3)]
    if matrix == dif:
        solucion = soluciondificil1
    if matrix == dificil2:
        solucion = soluciondificil2
    else:
        solucion = soluciondificil3

      
    







def impMatriz():
    for i in range(row):
        print(matrix[i])





#coloca la matriz en la interfaz con colores y botones
                
def coord(x, y):
    print("x:", x, "y:", y)
    global pos
    pos = (x,y)
    
    return pos
    

class BotonCoord(object):
    x = 0
    y = 0
    boton = None

    def __init__(self, x, y, ventana_principal, matrix):
        self.x = x
        self.y = y
        boton = Button(ventana_principal, text = matrix[y][x], command = lambda: ventana_principal.after(200, coord(self.x, self.y)))
        boton.grid(row = self.x, column = self.y)


def botones(ventana, matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            b = BotonCoord(j, i, ventana_principal, matriz)




def columnas(matriz,pos):
    global col
    col = []
    for fila in matriz:
        for num in fila:
            if fila.index(num) == pos[1]:
                col += [num]
   
    return col

def filas(matriz,pos):
    global fila
    for fila in matriz:
        if matriz[pos[0]] == fila:
            break
    
    return fila 
    
    
def cuadrantes(matriz,pos):
    x = pos[0] 
    y = pos[1]
    global cuadrante
    cuadrante = []
    if x in [0,1,2] and y in [0,1,2]:
        i = range(0,3)
        j = range(0,3)
    elif x in [3,4,5] and y in [0,1,2]:
        i = range(3,6)
        j = range(0,3)
    elif x in [6,7,8] and y in [0,1,2]:
        i = range(6,9)
        j = range(0,3)
    elif x in [0,1,2] and y in [3,4,5]:
        i = range(0,3)
        j = range(3,6)
    elif x in [3,4,5] and y in [3,4,5]:
        i = range(3,6)
        j = range(3,6)
    elif x in [6,7,8] and y in [3,4,5]:
        i = range(6,9)
        j = range(3,6)
    elif x in [0,1,2] and y in [6,7,8]:
        i = range(0,3)
        j = range(6,9)
    elif x in [3,4,5] and y in [6,7,8]:
        i = range(3,6)
        j = range(6,9)
    elif x in [6,7,8] and y in [6,7,8]:
        i = range(6,9)
        j = range(6,9)


    for indice in i:
        for indice2 in j:
            cuadrante.append(matriz[indice][indice2])

    return cuadrante
        
                
                   
                    

                    
                        
                

    
    

    
def moversudoku(matriz,e,pos,col,fila,cuadrante):
    if e not in col:
        if e not in fila:
            if e not in cuadrante:
                for f in matriz:
                    if matriz.index(f) == pos[0]:
                       if matriz[pos[0]][pos[1]]==0:
                           matriz[pos[0]].remove(0)
                        
                           f.insert(pos[1],e)
    else:
        print("messagebox error")
    


def perder():
    if 0 not in matrix:
        if matrix == solucion:
            messagebox.showinfo("Felicidades, usted ha ganado")
        else:
            messagebox.showinfo("Perdió,puede continuar o ver la solucion")



    moversudoku(ventana_principal, matrix,e,pos,col,fila)
    
#Formatea la hora en formato horas minutos y segundos

def format(elap):
    horas = (elap // 60) // 60
    minutos = (elap // 60) % 60
    segundos = elap % 60
    return str(horas) + ":" + str(minutos) + ":" + str(segundos)


def timeL(label):
    global ventana_principal, textoTiempo, tiempo
    textoTiempo = format(tiempo)
    label.config(text=textoTiempo)
    tiempo += 1
    if tiempo == 600:
        perder() == True
    print(tiempo)
    ventana_principal.after(1000, timeL, label)


 
#globaliza top10 y mejores jugadores
    
#topplayer = True



#cuando se quieren desplegar top player

def mejorjugsi():
    mejorjugador = True

def mejorjugno():
    mejorjugador = False

def conTimerSi():
    conTimer = True
def conTimerNo():
    conTimer = False 


def ventanaConfig():
    configwindow.geometry("500x500")
    configwindow.config(bg = "cyan")

   
    timersi = Button(configwindow, text="Desplegar Timer(Si)", command = lambda: configwindow.after(200,conTimerSi)) #desplegar timer
    timersi.place(x = 200, y = 100)
    
    timerno = Button(configwindow, text="Desplegar Timer (No)", command = lambda: configwindow.after(200,conTimerNo)) #deslpegar timer no
    timerno.place(x = 200, y = 150)

    
    facil = Button(configwindow, text="Nivel Fácil", command = lambda: configwindow.after(200, crearMatrixfacil)) #deslpegar top player si
    facil.place(x = 200, y = 200)

    
    medio = Button(configwindow, text="Nivel Medio", command= lambda: configwindow.after(200,crearMatrixmedio)) #desplegar top player no
    medio.place(x = 200,y=250)

    dificil = Button(configwindow, text="Nivel Difícil", command= lambda: configwindow.after(200,crearMatrixdificil)) #desplegar top player no
    dificil.place(x = 200,y=300)
               
               
    
    mainloop()
    
def ventanaJuego():
    #crearRandom()
    #crearRandom()

    # Ventana principal
    global ventana_principal
    ventana_principal = Tk()
    #ventanajuego

    botones(ventana_principal, matrix)

    ventana_principal.mainloop()

    
    ventana_principal.geometry("1000x1000") #dimensiones

    ventana_principal.config(bg="rosybrown1") #color de fondo
    

    # binding keyboard arrows, movimientos a las teclas
    """ventana_principal.bind("<Up>", upkey)
    ventana_principal.bind("<Down>", downkey)
    ventana_principal.bind("<Left>", leftkey)
    ventana_principal.bind("<Right>", rightkey)"""

    #si se quiere con timer despliega timer
    
    #if conTimer:
    l = Label(ventana_principal, textvariable=textoTiempo)
    l.place(x=500, y=450)
    timeL(l)
        
    movimiento = StringVar()

    #botones del juego

    entry = Entry(ventana_principal, fg="black", textvariable=movimiento)
    entry.place(x=700, y=425)

    b = Button(ventana_principal, text="Inserte su nombre", command=lambda: ventana_principal.after(200, imprimir(entry))) #nombre del jugador
    b.place(x=650, y=420)

    top = Button(ventana_principal, text="Ver Top 10", command=lambda: ventana_principal.after(200, windowtop10)) #top10
    top.place(x=520, y=400)

    continuar = Button(ventana_principal, text="Continuar", command=lambda: ventana_principal.after(200, print("Continua"))) #continuar jugando
    continuar.place(x=420, y=430)

    continuar = Button(ventana_principal, text="Guardar Partida", command=lambda: ventana_principal.after(200, lista10)) #guarda partida
    continuar.place(x=420, y=370)

    terminar = Button(ventana_principal, text="Terminar partida", command=lambda: ventana_principal.after(200, salir)) #termina partida
    terminar.place(x=480, y=300)

    uno = Button(ventana_principal, text="1", command=lambda: ventana_principal.after(200, moversudoku(matriz,1,pos,col,fila,cuadrante))) #termina partida
    uno.place(x=680, y=320)

    dos = Button(ventana_principal, text="2", command=lambda: ventana_principal.after(200, moversudoku(matriz,2,pos,col,fila,cuadrante))) #termina partida
    dos.place(x=680, y=290)

    tres = Button(ventana_principal, text="3", command=lambda: ventana_principal.after(200, moversudoku(matriz,3,pos,col,fila,cuadrante))) #termina partida
    tres.place(x=680, y=260)

    cuatro = Button(ventana_principal, text="4", command=lambda: ventana_principal.after(200, moversudoku(matriz,4,pos,col,fila,cuadrante))) #termina partida
    cuatro.place(x=680, y=230)

    cinco = Button(ventana_principal, text="5", command=lambda: ventana_principal.after(200, moversudoku(matriz,5,pos,col,fila,cuadrante))) #termina partida
    cinco.place(x=680, y=200)

    seis = Button(ventana_principal, text="6", command=lambda: ventana_principal.after(200, moversudoku(matriz,6,pos,col,fila,cuadrante))) #termina partida
    seis.place(x=680, y=170)

    siete = Button(ventana_principal, text="7", command=lambda: ventana_principal.after(200, moversudoku(matriz,7,pos,col,fila,cuadrante))) #termina partida
    siete.place(x=680, y=140)

    ocho = Button(ventana_principal, text="8", command=lambda: ventana_principal.after(200, moversudoku(matriz,8,pos,col,fila,cuadrante))) #termina partida
    ocho.place(x=680, y=110)

    nueve = Button(ventana_principal, text="9", command=lambda: ventana_principal.after(200, moversudoku(matriz,9,pos,col,fila,cuadrante))) #termina partida
    nueve.place(x=680, y=80)

    
    #if mejorjugador:
        #mj = Button(ventana_principal, text="Desplegar Mejor Jugador", command=lambda: ventana_principal.after(200, mejorjugador1)) #despliega el mejor jugador si
        #mj.place(x=340, y=330)
    #if not mejorjugador:
        #mj = Button(ventana_principal, text="Desplegar Mejor Jugador NO", command=lambda: ventana_principal.after(200, print("Mejor jugador es:NO "))) #mejor jug no
        #mj.place(x=320, y=430)

        
    
    #mover_matriz(ventana_principal, matrix)


    mainloop()


                                                                                                       

window()

