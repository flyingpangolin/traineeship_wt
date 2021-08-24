import random

#begin
aantal_dozen = 5
doos_met_kat = random.randint(1,aantal_dozen)
aantal_pogingen = 0
kat_gevonden = False

#start
while kat_gevonden == False:
    geen_goede_input = True
    while geen_goede_input:
        doos_openen = int(input(f"Welke doos wil je openen, kies 1 tot {aantal_dozen}?"))  # integer maken 
        if doos_openen > aantal_dozen or doos_openen <= 0:
            print("kies een nummer tussen 1 en 5")
        else:
            geen_goede_input = False

    aantal_pogingen= aantal_pogingen+ 1

    if doos_met_kat == doos_openen:
        kat_gevonden = True
        print(f"de kat is gevonden. In {aantal_pogingen} pogingen.") 
    else:
        print("de kat is nog niet gevonden")
        kat_gevonden = False
#verplaatsen
        if doos_met_kat == 1:
            doos_met_kat = doos_met_kat + 1
        elif doos_met_kat == 5:
            doos_met_kat = doos_met_kat -1
        else:
            keuze = [1,-1]
            doos_met_kat = doos_met_kat + random.choice(keuze)
            



    



  


