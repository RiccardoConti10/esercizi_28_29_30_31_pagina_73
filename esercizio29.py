print ("digita 3 per terminare l'elenco")
nomi = []
escursioni_termiche_delle_città = []
contatore = 0
while True:
    città = input ("nome della città:    ")
    temperatura_max = int (input ("la temperatura massima predefinita è di:    "))
    temperatura_min = int (input ("la temperatura minima predefinita  è di:    "))
    escursione_termica = (temperatura_max - temperatura_min)
    nomi.append (città)
    escursioni_termiche_delle_città.append (escursione_termica)
    temperatura == 0:
        for c in nomi:
            indice = nomi.index (c)
            temperatura_max_2 = int (input ("la temperatura massima di oggi è di:    "))
            temperatura_min_2 = int (input ("la temperatura minima di oggi è di:    "))
            escursione_termica_2 = (max_temperatura_2 - min_temperatura_2)

            if escursione_termica_2 > escursioni_termiche_delle_città [indice]:
                contatore += 1
        break
print ("oggi le città che hanno avuto  un'escursione termica maggiore rispetto alla predefinita sono", contatore)
