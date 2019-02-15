
print("Soy una calculadora,\n")
print("Dame dos numeros y una operacion(+,-,*,/,**)\n")

num1 = int(input())
num2 = int(input())
operacion = input()

if(operacion == '+'):
    print(num1 + num2)

elif(operacion == '-'):
    print(num1 - num2)

elif(operacion == '*'):
    print(num1 * num2)

elif(operacion == '/'):
    print(num1 / num2)

elif(operacion == '**'):
    print(num1 ** num2)
