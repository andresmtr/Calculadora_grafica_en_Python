#!/usr/bin/env python
# -*- coding: utf-8 -*-

#sirve para llama a la totalidad de la librería
from tkinter import *
from math import *

#raiz con el contenedor (en pocas palabras la variable que contiene la apliación en la parte grafica)
raiz=Tk()

#sirve para colocar titulo a la aplicación
raiz.title("Calculadora gráfica")

#tamaño por defecto del inicio de la applicación
raiz.geometry("392x500")

#para cambiar el color de fondo, bg significa background

raiz.config(bg="silver")

#se crea la funión para las operaciones

def BotonClick(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador)

#para limpiar los procesos de la calculadora

def clear():
    global operador
    operador=("")
    input_text.set("0")

#se crea la función para el igual

def operacion():
    global operador
    try:
        opera=str(eval(operador))#Sirve para visualizar en la pantalla
    except:
        clear()
        opera=("ERROR")
    input_text.set(opera)#Muestra e resultado

#Para sacar la raiz en la calculadora

def root():
    global operador
    operador = float(operador)
    operador = sqrt(operador)
    operador = str(operador)
    input_text.set(operador)
    operador = ""

#dimensiones de los botones
ancho_boton=7
ancho_boton2=16
alto_boton=3

#Se crea la varieable para la función
input_text=StringVar()
operador=""
clear()

#creación de botones
BotonAC=Button(raiz,text="AC",width=ancho_boton,height=alto_boton,command=clear).place(x=40,y=180)
BotonRaiz=Button(raiz,text="√",width=ancho_boton,height=alto_boton,command=root).place(x=120,y=180)
Boton_potencia=Button(raiz,text="x²",width=ancho_boton,height=alto_boton, command=lambda:BotonClick("**")).place(x=200,y=180)
Boton_division=Button(raiz,text="/",width=ancho_boton,height=alto_boton,command=lambda:BotonClick("/")).place(x=280,y=180)
Boton7=Button(raiz,text="7",width=ancho_boton,height=alto_boton,command=lambda:BotonClick(7)).place(x=40,y=240)
Boton8=Button(raiz,text="8",width=ancho_boton,height=alto_boton,command=lambda:BotonClick(8)).place(x=120,y=240)
Boton9=Button(raiz,text="9",width=ancho_boton,height=alto_boton,command=lambda:BotonClick(9)).place(x=200,y=240)
Boton_multiplicacion=Button(raiz,text="*",width=ancho_boton,height=alto_boton,command=lambda:BotonClick("*")).place(x=280,y=240)
Boton4=Button(raiz,text="4",width=ancho_boton,height=alto_boton,command=lambda:BotonClick(4)).place(x=40,y=300)
Boton5=Button(raiz,text="5",width=ancho_boton,height=alto_boton,command=lambda:BotonClick(5)).place(x=120,y=300)
Boton6=Button(raiz,text="6",width=ancho_boton,height=alto_boton,command=lambda:BotonClick(6)).place(x=200,y=300)
Boton_resta=Button(raiz,text="-",width=ancho_boton,height=alto_boton,command=lambda:BotonClick("-")).place(x=280,y=300)
Boton1=Button(raiz,text="1",width=ancho_boton,height=alto_boton,command=lambda:BotonClick(1)).place(x=40,y=360)
Boton2=Button(raiz,text="2",width=ancho_boton,height=alto_boton,command=lambda:BotonClick(2)).place(x=120,y=360)
Boton3=Button(raiz,text="3",width=ancho_boton,height=alto_boton,command=lambda:BotonClick(3)).place(x=200,y=360)
Boton_suma=Button(raiz,text="+",width=ancho_boton,height=alto_boton,command=lambda:BotonClick("+")).place(x=280,y=360)
Boton0=Button(raiz,text="0",width=ancho_boton2,height=alto_boton,command=lambda:BotonClick(0)).place(x=40,y=420)
Boton_coma=Button(raiz,text=",",width=ancho_boton,height=alto_boton,command=lambda:BotonClick(".")).place(x=200,y=420)
Boton_igual=Button(raiz,text="=",width=ancho_boton,height=alto_boton,command=operacion).place(x=280,y=420)

#es la donde se mostraran los resultados
Salida=Entry(raiz,font=('arial',20,'bold'),width=22,textvariable=input_text,bd=20,insertwidth=6,bg="powder blue",justify="right").place(x=40,y=60)


#sirve para que este constantemente abierta en forma de loop, debe estar en ultimo lugar
raiz.mainloop()
