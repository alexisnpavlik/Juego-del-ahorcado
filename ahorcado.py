import random
import os

def lectura():
    archivo=open("./data.txt","r",encoding="utf-8") 
    archivo= archivo.read()
    lista_palabras=archivo.split()
    return lista_palabras

def elegir_palabra():
    return random.choice(lectura())
    
def interfaz(palabra_correcta,respuesta):
    os.system ("cls")
    print("Adivina la palabra en el juego del ahorcado")
    for i in range(len(palabra_correcta)):
        respuesta.append("_")
        print(respuesta[i]," ",end="")


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