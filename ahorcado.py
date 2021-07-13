import random
import os
import re

def lectura():
    archivo=open("c:/Users/elbus/Documents/Python/Ahorcado/data.txt","r",encoding="utf-8") 
    archivo= archivo.read()
    lista_palabras=archivo.split()
    return lista_palabras

def elegir_palabra():
    return random.choice(lectura())
    
def interfaz(palabra_correcta,respuesta):
    respuesta=""
    os.system ("cls")
    print("Adivina la palabra en el juego del ahorcado")

    for i in range(len(palabra_correcta)):
        respuesta=respuesta+"_"
    print(palabra_correcta)


    while respuesta!=palabra_correcta:
        for i in respuesta:
            print(f"{i} ",end="")

        letra= input("\n\nIngresa una letra: ")


        for x in enumerate(palabra_correcta):
            if letra==x[1]:
                os.system ("cls")
                print("¡¡¡Corecto!!!!")

                print(type(x[0]))
                print(type(x[1]))
                e=x[0]
                f="ss"
                respuesta.replace("_",f) #grabe problema
                break
    
            
            else:
                os.system ("cls")
                print("¡¡¡Mala Suerte!!!!")
               
        



def comprobar_respuesta():
    pass

def run():
    lista_palabras=[]
    respuesta=[]
    lectura()
    palabra_correcta=elegir_palabra()
    interfaz(palabra_correcta,respuesta)


if __name__=='__main__':
    run()