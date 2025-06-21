inputUsuario = input("Introduce una palabra o frase: ")

inputUsuario = inputUsuario.lower()
inputUsuario = inputUsuario.replace(" ", "")
inputUsuario = inputUsuario.replace("á", "a")
inputUsuario = inputUsuario.replace("é", "e")
inputUsuario = inputUsuario.replace("í", "i")
inputUsuario = inputUsuario.replace("ó", "o")
inputUsuario = inputUsuario.replace("ú", "u")

invertir = inputUsuario[::-1]

if inputUsuario == invertir:
    print("Tu palabra o frase es un palíndromo")
else:
    print("Tu palabra NO es un palíndromo")