lunghezza = int (input ("scrivi il numero delle cifre binarie"))
totale = 0
for numero in range (lunghezza):
    cifra = int (input ("scrivi le cifre partendo da destra"))
    risultato = (cifra*2**numero)
    totale += risultato
print (totale)
