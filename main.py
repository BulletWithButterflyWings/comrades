choice = 0 
message = ""

#import datetime
#print (datetime.date())

while choice != 3:

    print("***Välkommen till loggboken***\n")
    print("1. Läs loggar ")
    print("2. Skriv en logg")
    print("3. Avsluta")

    try: 
        choice = int(input("\nGör ett val: "))
    except:
        print("Du gjorde inte ett korrekt val.")

    if choice == 1: 
        f = open('log.txt' , 'r')
        for line in f:
                print(line)
        f.close()          
    elif choice == 2:
        f = open('log.txt' , 'a+')
        f.write(input("Skriv: ")) 
        f.close()
    else:
        print("\nStänger av programet...")