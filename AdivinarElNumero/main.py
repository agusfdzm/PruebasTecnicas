import random

numeroAleatorio = random.randint(1, 50)

intentos = 3

while intentos > 0:
    intento = int(input("Adivina el numero aleatorio: "))

    if intento == numeroAleatorio:
        print("ENHORABUENA. HAS ADIVINADO EL NUMERO")
        break
    else:
        intentos = intentos - 1
        print(f"Te quedan {intentos} intento/s")

        if intento < numeroAleatorio:
            print("El numero que tienes que adivinar es mayor")
        else:
            print("El numero que tienes que adivinar es menor")
    
    if intentos == 0 and intento != numeroAleatorio:
        print(f"HAS FALLADO! El numero aleatorio era {numeroAleatorio}")