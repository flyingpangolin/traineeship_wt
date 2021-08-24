#importeer de json file met de dictionary
import json
json_file = open('Dieren_JSON.json', 'rt')
dieren = json.loads(json_file.read())
json_file.close()

def start_spel():
    print('Neem een dier in gedachte..')
    spel_starten = ja_of_nee('Wil je het spel starten?')
    if spel_starten == 'ja':
        #start de formule met de recursie, met dictionary 'dieren' als parameter
        vragen(dieren)


def vragen(tak):
    #de functie formatting zorgt dat elke vraag een hoofdletter en vraagteken heeft
    vraag = formatting(tak)
    antwoord_vraag = ja_of_nee(vraag)

    # controleren of een tak eindigt met een dier of nog een vraag
    uitkomst = isinstance(tak[antwoord_vraag], dict)
    #volgende vraag stellen
    if uitkomst:
        vragen(tak[antwoord_vraag])
    #uitkomst dier geven
    else:
        antwoord_einde = ja_of_nee('Dacht je aan een '+ tak[antwoord_vraag]+'?')
        if antwoord_einde == 'ja':
            print('Hoera! Ik had het goed geraden!')
            opnieuw_spelen()
        else:
            #maak een nieuw dier
            nieuw_dier(tak, antwoord_vraag)
            opnieuw_spelen()


#vragen format (vraagtekens, hoofdletters)
def formatting(tak):
    vraag = tak['vraag'].capitalize()
    if vraag.endswith('?'):
        return vraag
    else:
        vraag += '?'
        return vraag

#ja of nee invullen
def ja_of_nee(vraag):
    antwoord = input(vraag + ' ')
    if antwoord.startswith('j'):
        antwoord = 'ja'
        return antwoord
    else:
        antwoord = 'nee'
        return antwoord

def nieuw_dier(tak, richting):
    oud_dier = tak[richting]
    antwoord_nieuw_dier = input('Aan welk dier dacht je dan? ').lower()
    #'een ' weghalen als het voor de naam van het dier is getypt
    if antwoord_nieuw_dier.startswith('een '):
        antwoord_nieuw_dier = antwoord_nieuw_dier.replace('een ', '')
    #een nieuwe vraag laten invullen en evt vraagtekens en punten weghalen
    vraag_nieuw_dier = input(f'Welke vraag had ik moeten stellen om {antwoord_nieuw_dier} te kunnen raden in plaats van {oud_dier}?').lower().replace('?', '').replace('.', '')
    tak[richting] = {'vraag': vraag_nieuw_dier, 'ja': antwoord_nieuw_dier, 'nee': oud_dier}

def opnieuw_spelen():
    opnieuw = ja_of_nee('Wil je nog een keer spelen?')
    if opnieuw == 'ja':
        vragen(dieren)
    else:
        aanpassen = ja_of_nee('Jammer! Is er een vraag gesteld die je aan zou willen passen?')
        if aanpassen == 'ja':
            vragen_lijst(dieren)
            vragen_nummeren(vragen_array, vraag_nummer)
            vraag_aanpassen()
            vragen_updaten(dieren, vragen_array)


#vragen aanpassen

vragen_array = []
vraag_nummer = 1

#alle vragen verzamelen in een array
def vragen_lijst(tak):
    if isinstance(tak, dict):
        vraag = formatting(tak)
        vragen_array.append(vraag)
        for richting in tak:
            vragen_lijst(tak[richting])

#alle vragen printen met een bijbehorend nummer
def vragen_nummeren(vragen_array, vraag_nummer):
    for vraag in vragen_array:
        print(vraag_nummer, ':', vraag)
        vraag_nummer +=1

def vraag_aanpassen():
    vraag_nummer = int(input('welke vraag wil je aanpassen?'))
    nieuwe_vraag = input('vul de nieuwe vraag in: ')
    vragen_array[vraag_nummer-1] = nieuwe_vraag

def vragen_updaten(tak, vragen_array):
    if isinstance(tak, dict):
        tak['vraag'] = vragen_array[0].lower().replace('?', '').replace('.', '')
        del vragen_array[0]
        for richting in tak:
            vragen_updaten(tak[richting], vragen_array)


def vragen_updaten_los():
    vragen_lijst(dieren)
    vragen_nummeren(vragen_array, vraag_nummer)
    vraag_aanpassen()
    vragen_updaten(dieren, vragen_array)

start_spel()
#vragen_updaten_los()


#nieuwe dictionary opslaan

json_einde = open('Dieren_JSON.json','wt')
json_einde.write(json.dumps(dieren))
json_einde.close()

