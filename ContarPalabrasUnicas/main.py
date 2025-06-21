inputUser = input("Introduce un texto: ")

inputUser = inputUser.replace(".", "")
inputUser = inputUser.replace(",", "")
inputUser = inputUser.replace("!", "")
inputUser = inputUser.replace("?", "")

palabras = inputUser.split()

frecuencia = {}

for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

print(f"Tu lista de palabras: {frecuencia}")