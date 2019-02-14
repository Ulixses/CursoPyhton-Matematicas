# Descripción: Juego para adivinar un número secreto

import random # Este paquete es necesario para generar números aleatorios

print("Hola, vamos a jugar a adivinar un número secreto entre 1 y 100")

# Elegir al azar un número entero entre 1 y 100
numero_secreto = random.randrange(1,101)

print("Ya lo he pensado, podemos empezar")
intentos = 0            #Contador de intentos. Empieza en cero
acierto = False         #Variable bool para ver cuando ganas. Empieza en false

# Bucle principal del programa. Mientras el usuario no adivine el número repetimos
# la jugada e incrementamos el número de intentos
while not(acierto):
    intentos = intentos + 1 #Cada vez que metes un numero te aumenta un intento
    #Pedimos un numero al usuario en cada intento
    numero_humano = int(input("¿Qué numero has pensado?: "))
    
    if (numero_humano == numero_secreto):
        print("¡Enhorabuena, has acertado!. Número de intentos:",intentos)
        acierto = True
    else:
        #Damos una pista al usuario si falla
        if (numero_humano < numero_secreto):
            print("El número que pensé es mayor que el tuyo")
        else:
            print("El número que pensé es menor que el tuyo")
        print("Has utilizado",intentos,"intentos")
                        
    
