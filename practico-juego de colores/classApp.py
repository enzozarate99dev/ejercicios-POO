
import time
from tkinter import *
import tkinter as tk
import random
import winsound

class App:
    __ventana: object
    __colores: list
    __secuencia: list
    __secuenciaJugador: list
    __puntos: int
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title("Juego Simon")
        self.__colores = ['red', 'green', 'blue', 'yellow']
        self.__botones =[]
        self.__secuencia = [] 
        self.__secuenciaJugador = []
        self.__puntos = 0
        self.crearTablero()
        self.siguienteRonda()

        
    def crearTablero(self):
        self.canvas_frame = tk.Frame(self.__ventana)
        self.canvas_frame.pack()
        
        rojo = self.crearBoton(self.canvas_frame, "red", 0, 0)
        verde = self.crearBoton(self.canvas_frame, "green", 0, 1)
        azul = self.crearBoton(self.canvas_frame, "blue", 1, 0)
        amarillo = self.crearBoton(self.canvas_frame, "yellow", 1, 1)
        self.__botones.append(rojo)
        self.__botones.append(verde)
        self.__botones.append(azul)
        self.__botones.append(amarillo)

        self.marcadorPuntos = tk.Label(self.__ventana, text="Puntaje: 0")
        self.marcadorPuntos.pack(pady=10)
    def crearBoton(self, frame, color, row, column):
        canvas = tk.Canvas(frame, width=200, height=200, bg=color, relief="raised", bd=5)
        canvas.grid(row=row, column=column, padx=10, pady=10)
        canvas.bind("<Button-1>", self.onClick) # asocia el click izq con el mtodo onclick
        return canvas
    
    def onClick(self, event):
        boton = event.widget #se refiere al Canvas (boton) que fue clicado.
        color = boton.cget("bg")
        self.cambiarBoton(boton)
        self.__secuenciaJugador.append(color)
        self.compararSecuencias()

    def cambiarBoton(self, boton):
        boton.config(relief="sunken")
        self.__ventana.update()
        self.__ventana.after(200, lambda: boton.config(relief="raised"))
    
    
    def compararSecuencias(self):
        if self.__secuenciaJugador == self.__secuencia[:len(self.__secuenciaJugador)]:
            if len(self.__secuenciaJugador) == len(self.__secuencia):
                self.__puntos += 1
                self.actualizarPuntos()
                self.siguienteRonda()
        else:
            self.finalizar()
   
    def actualizarPuntos(self):
        self.marcadorPuntos.config(text=f"Score: {self.__puntos}")

    def siguienteRonda(self):
        self.__ventana.after(1000, self.añadirColor)
        self.__ventana.after(2000, self.recorrerSecuencia)
        self.__secuenciaJugador = []

    def añadirColor(self):
        self.__secuencia.append(random.choice(self.__colores))
    def recorrerSecuencia(self):
        i = 0
        while i < len(self.__secuencia):
            color = self.__secuencia[i]
            self.__ventana.after(i * 700, lambda color=color: self.parpadear(color))
            i += 1
        self.__ventana.update()
    def parpadear(self, color):
        for btn in self.__botones:
            if btn.cget("bg") == color:
                self.cambiarBoton(btn)
    def finalizar(self):
        self.marcadorPuntos.config(text=f"GAME OVER. Puntaje Final : {self.__puntos}")
        self.__secuencia = []
        self.__secuenciaJugador = []
        self.__puntos = 0
        self.__ventana.after(3000, self.siguienteRonda)

    def ejecutar(self):
        self.__ventana.mainloop()


if __name__ == "__main__":
    juego = App()
    juego.ejecutar()
    
