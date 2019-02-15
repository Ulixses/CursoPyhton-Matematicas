#bucles 
a = 10 #a empieza en 10
listaCompra = ["potato","mandarinas","chocolate"]
print("\nEmpieza el primer bucle") # "\n" hace un salto de linea como la tecla ENTER
while(a >= 0): #Este bucle seguira hasta que a >= 0
    print(a) #Mostramos a
    a = a - 1 #Restamos 1 pra que el bucle pueda acabar
    
print("\nEmpieza el segundo bucle")
for i in range(5,10): #En este caso la i ira desde 5 hasta 10 - 1
    print(i)

print("\nEmpieza el tercer bucle")
for i in range(10): #En este caso la i ira desde 0 hasta 10 - 1
    print(i)

print("\nEmpieza el cuerto bucle")
for i in listaCompra: #En este caso la i coje los valores de la lista hasta que se acabe
    print(i) 
