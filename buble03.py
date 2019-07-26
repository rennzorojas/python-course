#import os Sirve para importar la librería
import os
resp = ""
sue = 0
con = 0
ph = 37

#while indica que lo que hay bajo él se va a repetir hasta donde se lo programe
while resp!="N":
    nom = input("Nombre del empleado:")
    ht = int(input("Ingrese las HT"))
    sue = ht * ph

    #con+=1 es un contador de ciclos
    con+=1
    print("El Pago ha recibir es:"+str(sue))
    
    #"Desea continuar" alude a que continuará hasta que respuesta sea N: resp!="N", y sale del bucle
    resp=input("Desea Continuar?")

    #función CLS sirve para limpiar pantalla para continuar sgte ciclo
    os.system("cls")

#Imprime la cantidad de bucles
print("La cantidad de empleados procesados")