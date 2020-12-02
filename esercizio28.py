from random import randint
lancio1 = randint (1, 12)
lancio2 = randint (1, 12)
lancio3 = randint (1, 12)
print ( "partecipano ad una gara di lancio del peso studentesca, tre studenti")
print ("il primo studente ha fatto un lancio di", lancio1,"metri, il secondo studente ha fatto un lancio di", lancio2, "metri, il terzo studemte ha fatto un lancio di", lancio3, "metri" )
if lancio1 > lancio2 and lancio3 :
    print ("il vincitore è il primo studente, avendo fatto un lancio di", lancio1, "metri")
elif lancio2 > lancio1 and lancio3 :
    print ("il vincitore è il secondo studente avendo fatto un  lancio di", lancio2, "metri")
elif lancio3 > lancio2 and lancio1 :
    print ("il vincitore è il secondo studente avendo fatto un lancio di", lancio3, "metri")
