choice = 0 # Ger "choice" värdet 0.

#import datetime
#print (datetime.date())

while choice != 4: # Loopar allt understående till man trycker avsluta (3).

    print("***Välkommen till loggboken***\n") # Skriver ut menyn i terminalen.
    print("1. Läs loggar ") 
    print("2. Skriv en logg") 
    print("3. Rensa logg")
    print("4. Avsluta") 

    try: # Felsöker programet så att man undviker kraschar i koden.
        choice = int(input("\nGör ett val: ")) # Sparar det du skriver in i variabeln "choice". 
    except: # Ifall du skriver in en bokstav, så säger den åt dig att skriva om.
        print("Du gjorde inte ett korrekt val.") #

    if choice == 1: # Ifall du väljer alternativ 1 så skrivs understående ut.
        f = open('log.txt' , 'r') # Öppnar upp filen "log.txt" med full rättighet för ändringar.
        for line in f: # Den säger åt att printa varje linje i textloggen.
                print(line) # Skriver ut raden från log.txt.
        f.close()          # Stänger log.txt. 
   
    elif choice == 2: # Ifall du väljer alternativ 2 så sker understående. 
        f = open('log.txt' , 'a+') # Du öppnar log.txt, med a+(append) som gör att det skrivs ut på nya rader varje gång.
        f.write(input("Skriv: ")) # Du kan skriva i dokumentet (log.txt).
        f.close() # Stänger textfil (log.txt).
    
    elif choice == 3:
        f = open('log.txt' , 'w+')
        f.write("")
    else: # Om inte 1 eller 2 skrivs in så stängs programet.
        print("\nStänger av programet...") 