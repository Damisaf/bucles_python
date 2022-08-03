# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA:
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio
operaciones_validas = ["+", "-", "*", "/", "**", "FIN"]

while True:
    while True:
        numero_1 = input('Ingrese el primer número: ')
        if not numero_1.isdigit():
            print("ingreso incorrecto - solo debe igresar numeros!")
        else:
            break
    while True:
        numero_2 = input('Ingrese el segundo número: ')
        if not numero_2.isdigit():
            print("ingreso incorrecto - solo debe igresar numeros!")
        else:
            break
    valida = False
    while True:
        operacion = input("Ingrese la operacion a realizar [+] [-] [*] [/] [**] [FIN]: ")
        for i in operaciones_validas:
            if operacion == i:
                valida = True
                break
        if not valida:
            print("operador no valido")
            continue
        else:
            break
    numero_1 = int(numero_1)
    numero_2 = int(numero_2)

    if operacion == "+":
        resultado = numero_1 + numero_2
        print(numero_1, "+", numero_2, "es: ")
    elif operacion == "-":
        resultado = numero_1 - numero_2
        print(numero_1, "-", numero_2, "es: ")
    elif operacion == "*":
        resultado = numero_1 * numero_2
        print(numero_1, "*", numero_2, "es: ")
    elif operacion == "/":
        if numero_2 == 0:
            print("operacion no valida")
            continue
        else:
            resultado = numero_1 / numero_2
            print(numero_1, "/", numero_2, "es: ")
    elif operacion == "**":
        resultado = numero_1 ** numero_2
        print(numero_1, "**", numero_2, "es: ")
    elif operacion == "FIN":
        break
    print(resultado)
