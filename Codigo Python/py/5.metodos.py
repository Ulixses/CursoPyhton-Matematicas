def metodo(var1,var2,caracter):
    #el def indica que es un metodo, el nombre de este metodo en este caso sera metodo y recibe tres veriables
    suma = var1 + var2
    resta = var1 - var2
    multiplicacion = var1 * var2 
    #este metodo hara una suma una resta y una multiplicación con los parametros que recibe
    if (caracter == '+'):
        return suma
    #si el caracter que se ha introduciodo es una suma devuelve la suma
    elif (caracter == '-'):
        return resta
    #si el caracter que se ha introducido es una resta devuelve la resta
    elif(caracter == '*'):
        return multiplicacion 
    #si el caracter que se ha intrudico es una multiplicacion devuelve la multiplicacion
print(metodo(2,2,'*'))
