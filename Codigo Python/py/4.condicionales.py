#condicionales y booleanos
a = True #Asi se declaran variables bool que pueden tener los valores(True/False)
b = False#Cambia las variables para ver como cambia el funcionamiento

if(a): 
    print("a es verdadero")
elif(b): #Solo prueba esta condicion si las anteriores son falsas
    print("a es falsa b es verdadera")
else: #Si todo lo anterior es falso entra aqui siempre
    print("a y b son falsas")


if(a or b): #El operador or funciona si alguno es True
    print("a es verdera o b es verdadera o las dos son verdaderas\n")
    if(a):
        print("a es verdadera\n")
    elif(b):
        print("b es verdadera\n")
if(a and b): #El operador and funciona solo si todo es True
    print("a y b son verdaderas")


num1 = 1 #Cambia las variables para ver como cambia el funcionamiento
num2 = 3

if(num1>num2):
    print(num1 ,'>' , num2)
elif(num1 == num2):
    print(num1 , ' = ' , num2)
else:
    print(num1 , '<' , num2)
