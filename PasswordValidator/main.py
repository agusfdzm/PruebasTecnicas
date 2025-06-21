contraseña = input("Validar contraseña: ")

check = 0

if (len(contraseña) >= 8):
    for letra in contraseña:
        if (letra.isupper() == True):
            check = check + 1
            break
    for letra in contraseña:
        if (letra.isnumeric() == True):
            check = check + 1
            break
else:
    print("Contraseña demasiado corta")

if (check == 2):
    print("Tu contraseña es segura")
else:
    print("Tu contraseña no es segura")