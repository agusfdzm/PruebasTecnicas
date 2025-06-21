frase = input("Introduce una frase: ")

noEspacios = frase.replace(" ", "")

vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
consonantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]


numVocales = 0
numConsonantes = 0

for letra in noEspacios:
    letra = letra.lower()
    if letra in vocales:
        numVocales += 1
    elif letra in consonantes:
        numConsonantes += 1

print(f"Tu frase tenía  {numVocales} vocales y {numConsonantes} consonantes.")