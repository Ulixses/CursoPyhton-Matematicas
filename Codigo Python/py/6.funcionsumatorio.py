# -*- coding: utf-8 -*-
def sumatorio(num):
    sum = 0
    #establezco la variable sum
    for i in range (0,num+1):
        #hago un bucle de cero hasta el numero más uno ya que el intervalos es abierto 
        sum = sum + i
        #sumo i a sum
    return sum
print(sumatorio(8))