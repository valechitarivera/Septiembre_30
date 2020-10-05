#Crear menú con 3 opciones
#1. Opcion 1: Temperaturas
#2. Opcion 2: Datos de Personas
#3. Opción 3: Salir
import os 

def Temperaturas():                         #definición de función
    print("****** TEMPERATURAS *****")

    pausa=input("Presione una tecla para continuar")

def Personas():
    print("****** DATOS DE PERSONAS ******")

    pausa=input("Presione una tecla para continuar")

seguir=True 
while seguir:
    os.system('cls')
    print ("1. Temmperaturas")
    print ("2. Datos de Personas")
    print ("3. Salir")
    op=int(input("Ingrese opción 1,2,3: "))
    if(op==1):
        Temperaturas()          #invocar o llamar a una función
    elif (op==2):
        Personas()
    else:
        print("Finalizar")
        break