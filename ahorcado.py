def lectura():
    lista_palabras=[]
    archivo=open("./data.txt","r",encoding="utf-8") #arreglar despues
    archivo= archivo.read()
    lista_palabras=archivo.split()

    print(lista_palabras)

def elegir_palabra():
    pass

def interfaz():
    pass

def comprobar_respuesta():
    pass

def run():
    lectura()
if __name__=='__main__':
    run()