import random
import os

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
        respuesta_2=[]


    while respuesta!=palabra_correcta:
        for i in respuesta:
            print(f"{i} ",end="")

        letra= input("\n\nIngresa una letra: ")
        letra=letra.lower()
        os.system ("cls")

        for x in enumerate(palabra_correcta):
            if letra==x[1]:
            
                os.system ("cls")
                print("¡¡¡Corecto!!!!")
                
                respuesta_2=list(respuesta)
                respuesta_2[x[0]]=letra
                respuesta=""
                respuesta= "".join(respuesta_2)
                
        
    print(f"LOGRASTE ADIVINAR LA PALABRA, FELICIDADES!!! \n La palabra era: {palabra_correcta}")
        

def run():
    lista_palabras=[]
    respuesta=[]
    lectura()
    palabra_correcta=elegir_palabra()
    interfaz(palabra_correcta,respuesta)


if __name__=='__main__':
    run()