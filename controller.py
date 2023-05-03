# -*- coding: utf-8 -*-
"""
Created on Tue May  2 10:01:10 2023

@author: lab
"""

class robotController:
    def __init__(self,modelo,vista):
        self.modelo=modelo
        self.vista=vista
    def compilar(self):
        while True:
            print("")
            print("robot encendido ")
            self.vista.oracion("""1. Mover ; 2. Detener; 3. salir""")
            self.vista.oracion("ingrese comando")
            c=input().lower()
            if(c==1):
                self.mover()
            elif c==2:
                print("")
                print("robot deteniddo")
                print("")
            elif c==3:
                break
            else:
                print("")
                print("Actividad no valida")
                print("")

    def mover(self):
        elevacion=self.vista.get_user_input()
        rotacion=self.vista.get_user_input()
        longitud=self.vista.get_user_input()
        self.modelo.move_elevation(elevacion)
        self.modelo.move_rotation(rotacion)
        self.modelo.move_longitud(longitud)
        self.modelo.movimiento=True
        self.vista.mostrar(self.modelo.elevacion,self.modelo.rotacion,self.modelo.longitud,self.modelo.movimiento)
    
    