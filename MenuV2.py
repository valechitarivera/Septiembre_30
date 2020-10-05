#Valentina Rivera
#Crear menú con tres opciones: 
#1. Opción 1: Temperaturas
#2. Opción 2: Datos de Personas
#3. Opción 3: Salir 
import os 

def Temperaturas():                         #definición de función
    print("****** TEMPERATURAS *****")
    #Ingresar n temperaturas donde n es un número ingresado por teclado 
    #mostrar el promedio de las temperaturas ingresadas
    suma=0
    veces=int(input("Ingrese cantidad de temperaturas: "))
    for x in range(veces): #va a ingresar según la cantidad ingresada en la variable veces, dato entero.
        tempe=float(input("Ingrese una temperatura: "))
        suma=suma+tempe
    
    print("El promedio de las temperaturas ingresadas es: " , round((suma/veces),2))

    pausa=input("Presione una tecla para continuar")

def Personas():
    print("****** DATOS DE PERSONAS ******")
    #ingresar para n personas donde n es un número ingresado por teclado: 
    #nombre y edad. Mostrar cuantas personas son mayores de edad y cuantas son menores de edad
    #subir a github la segunda version de lo programado con el siguiente commit:
    #"Se agrego opcion 2 al menu de python"
    menor=0
    mayor=0
    

    total=int(input("Ingrese cantidad de personas: "))
    for x in range(total):
        perso=""
        perso=str(input("Ingrese nombre de la persona: "))
        
        edad=int(input("Ingrese edad de la persona: "))
        if(edad>17):
            mayor=mayor+1
        elif(edad<=17):
            menor=menor+1
    print("La cantidad de personas ingresadas que son mayores de edad son: "+str(mayor))
    print("La cantidad de personas ingresadas que son mayores de edad son: "+str(menor))

    pausa=input("Presione cualquier tecla para continuar")




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
     