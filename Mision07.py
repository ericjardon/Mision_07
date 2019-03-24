#Autor: Eric Andrés Jardón Chao
#Misión 07: Dos funciones con ciclos while.

def main():
    opcion=0
    while opcion != 3: #La opción 3 indica salir del menú
        print("Misión 07. Ciclos while.\nAutor: Eric Andrés Jardón Chao\nMatrícula A01376748.")
        print("Teclee la opción que desea ejecutar.\n"
              "1. Calcular divisiones.\n2. Encontrar valor mayor.\n3. Salir.")
        opcion = int(input("Teclea tu opción: "))
        if opcion == 1:
            probarDivisiones()
        elif opcion == 2:
            encontrarMayor()
        elif opcion !=3:
            print("ERROR: Trate con una opción válida.")
    print ("¡Regresa pronto!") #Al finalizar el programa se despide.


def probarDivisiones():
    dividendo=int(input("Teclea el número a dividir (entero positivo)"))
    divisor=int(input("Teclea el divisor (entero positivo)"))
    dividir(dividendo,divisor)

def dividir(dividendo,divisor):
    cociente=0 #inicializa el contador
    resta=dividendo #La cantidad que queda cada vez que le restamos el divisor
    residuo=dividendo #valor default
    if divisor>0:
        while resta>=0: #Mientras la resta sea positiva seguimos restando
            resta=resta-divisor
            if resta>=0: #Si la resta es positiva, añadimos 1 al contador de cociente.
                cociente+=1
                residuo=resta #Cada vez que restemos uno, el residuo es la cantidad que queda. Así, cuando se detiene el ciclo es el último número antes de volverse negativo.
        print("%d / %d = %d, sobra %d"%(dividendo,divisor,cociente,residuo)) #imprime el resultado
    else:
        print("Error: Cálculo imposible (teclee números enteros positivos)")

def encontrarMayor():
    Mayor=0 #El número referencia para comparar
    numero=Mayor #Para que sea diferente de -1
    print("Teclea una serie de números enteros positivos para encontrar el mayor.")
    while numero!=(-1):
        numero=int(input("Teclea un número [-1 para salir]: "))
        if numero<0 and numero!=(-1): #Si el número es negativo, devuelve error.
            print("Error: teclea valores enteros positivos.")
        if numero>Mayor: #Si el número ingresado es mayor al de referencia, lo guardamos como el nuevo mayor de referencia..
            Mayor=numero
        else: #Si no es mayor, lo ignoramos.
            pass
    if Mayor>0: #si el número resultante es mayor a cero, lo imprime.
        print("El mayor es",Mayor)
    if Mayor == 0: #Si el valor mayor continúa siendo cero, no hay un valor mayor como tal. (en teoría es cero, pero qué chiste)
        print("No hay valor mayor")

main()