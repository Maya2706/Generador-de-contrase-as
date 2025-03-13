import random
def generar_contraseña(longitud):
    elements = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(longitud):
        password += random.choice(elements)
    return password
long = int(input("Introduzca la longitud del password: "))
print(generar_contraseña(long))