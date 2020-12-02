list = []
numero = int (input ("dimmi un numero naturale"))
while True:
    quoziente_del_numero_scelto = int (numero/2)
    resto_del_numero_scelto = numero % 2
    if resto_del_numero_scelto == 1:
       list.append (1)
    else:
        list.append (0)
    numero = quoziente_del_numero_scelto
    
    if quoziente_del_numero_scelto == 0:
        break
list.reverse ()
print (list)
