edad = 0
while edad <18:
    edad = edad + 1
    if (edad % 2) == 0:
        continue
        #break cuando ubicado el resultado deseado se detiene el bucle
    print ("Felicidades, tienes "+str(edad))