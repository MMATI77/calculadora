print("Bienvenido a la calculadora de Matias Birocco")
#print("Elige la operación a realizar con la primer letra de la operación")
n1 = float(input("Ingresa el primer número: "))
n2 = float(input("Ingresa el segundo numero: "))
letra = input("Que deseas hacer con los dos números, presiona la leta\n\
S s=Suma\n\
R r=Resta\n\
M m=Multiplicación\n\
D d=División\n\
Presiona la letra: ").lower()
res = 0
if letra == "s":
    print(f"La suma de {n1}+{n2} = {n1+n2}")
elif letra == "r":
    print(f"La resta de {n1}-{n2} = {n1-n2}")
elif letra == "m":
    print(f"La multiplicación de {n1}X{n2} = {n1*n2}")
elif letra == "d":
    if n2 == 0:
        print("Matemáticamente no se puede dividir entre cero(0) --Menso--")
    else:
        print(f"La división de {n1} / {n2} = {n1/n2}")
else:
    print(f"Tenes que ingresar la primer letra de la operación a realizar, estupido. \n\
la letra {letra.upper()} que ingresaste no existe TENES UN MENU EN LA PARTE DE ARRIBA")
    quit()