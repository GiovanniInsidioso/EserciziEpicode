nome_scuola = 'Epicode'
print (nome_scuola[0:3]) 


nome_scuola = 'Epicode'
maiuscolo = nome_scuola.upper()
print (maiuscolo)

#metodo 1
x = 10
b = 2
c = 3
x = (x+b)*3
print (x)

#metodo
x= 10
while x<12:
    x=x+1
    x= x*3 + 3
    print (x)

    
    efficienza = 18
    costo = 1.90
    viaggio = 100
    carburante = viaggio/efficienza
    costo_viaggio = carburante*costo
    print('€', costo_viaggio)

    #scriviamo un programma che chiede in input all'utente una stringa e visualizza 
    #i primi 3 caratteri, seguiti da 3 punti di sospsensione e quindi ultimi 3 caratteri

    stringa = input("Inserisci la stringa che vuoi manipolare:\n")
    print(stringa[0:3] + "..." + stringa [-3:])

    # verificare, per ognuna delle seguenti stringhe,
    #se il numero di caratteri è compreso tra 5 e 8
    lista_stringhe = ['Epicode', 'Windows', 'Excel', 'PowerPoint', 'Word']
    for i in lista_stringhe:
        print("La lunghezza della parola '", i , "' è :", len(i))
    if 5 <=len(i) <= 8:
        print("compreso\n")
    else:
        print("non compreso\n")

        #abbiamo una lista di codici prodotto. Per ognuno estrarre la parte finale
        # trattino incluso e memorizzarlo in una variabile

        codici = ["knt-61", "cha-69", "qtr-78"]
        cod1 = codici[0][-3:]
        cod2 = codici[1][-3:]
        cod3 = codici[2][-3:]
        print(cod1, " ",cod2, " ", cod3)