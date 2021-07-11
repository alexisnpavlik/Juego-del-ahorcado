import random

def lectura():
    archivo=open("./data.txt","r",encoding="utf-8") 
    archivo= archivo.read()
    lista_palabras=archivo.split()
    return lista_palabras

def elegir_palabra():
    return random.choice(lectura())
    
def interfaz():
    pass

def comprobar_respuesta():
    pass

def run():
    lista_palabras=[]
    lectura()

    print(elegir_palabra()) #problema de lista vacia

if __name__=='__main__':
    run()