choice = 0 
message = ""
meny = 0

#import datetime
#print (datetime.date())

while meny != 3:

    print("***Välkommen till loggboken***.\n")
    print("1. Läs loggar ")
    print("2. Skriv en logg")
    print("3. Avsluta")

    try: 
        meny = int(input("Gör ett val: "))
    except:
        print("Du gjorde inte ett korrekt val.")
