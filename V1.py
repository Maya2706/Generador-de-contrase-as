import random
caracteres = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
contrs = ""
x = int(input("Escribe la longitud de tu contraseña: "))

if x < 5:
    while True:
       x = int(input("Tu contrase;a es demasiado corta, escribe la longitud de tu contrase;a denuevo: "))
       if x > 5:
           break


for i in range(x):
    caracter_aleatorio = random.choice(caracteres)
    contrs += caracter_aleatorio


print("Contraseña generada", contrs)