import time
import json
import random

# opvragen dict
verzoek = 'Antwoord alleen met ja of nee...'
f = open('database.txt', 'r')
jdata = f.read()
dieren = json.loads(jdata)
f.close()

#opmaak database
def addstuff(dieren):
    if isinstance(dieren, dict):
        for k,v in dieren.items():
            if k == 'vraag':
                dieren['vraag'] = v.capitalize() + "?"
            else: addstuff(v)
    return dieren

def removestuff(dieren):
    if isinstance(dieren, dict):
        for k,v in dieren.items():
            if k == 'vraag':
                dieren['vraag'] = v[:-1].lower()
            else: removestuff(v)
    return dieren

#functies om het spel te spelen
def dictomaker(Odier, Nvraag, Ndier, data, plaats):
    data[plaats] = {
        'vraag': Nvraag,
        'ja': Ndier,
        'nee': Odier
    }

def save_the_animal(data, Odier, plaats):
    Ndier = input( 'Ik heb het dier helaas niet kunnen raden, \nmaar jij kan me helpen!\nWelk dier had je in gedachten? ').lower().strip()
    if 'een' in Ndier: Ndier = Ndier[4:]
    while True:  
        vraag = input(f'Wat is een karakteristiek dat een {Odier} niet heeft en een {Ndier} wel? ').strip().lower()
        if vraag.startswith("een "): 
            Nvraag = f"Heeft het dier {vraag}? "
            break
        elif len(vraag.split()) > 2:
            print("Oeei... ik begrijp niet helemaal wat je bedoelt. \nGeef een kort antwoord van 1 a 2 woorden.")
            continue
        elif vraag.endswith('en'): 
            Nvraag = f"Heeft het dier {vraag}? "
            break
        else: 
            Nvraag = f"Heeft het dier een {vraag}? "
            break
    dictomaker(Odier, Nvraag, Ndier, data, plaats)
    print(random.choice(['Gracias', 'Thank you', 'Yeah']))
    print('De vraag is nu: '+ Nvraag)
    x = vraagloop('Wil je de vraag aanpassen?')
    if x == True:
        updatevraag(dieren)
    restart()

def start(data):
    print('Hee jij daar! Bedenk een dier...')
    time.sleep(2)
    print('Ben je er klaar voor? ')
    print(verzoek)
    vraag1(data)

def antwoord(jon):
    jon = jon.lower().strip()
    if jon == 'ja':
        return(True, True)
    elif jon == 'nee':
        return True, False
    else:
        print(verzoek)
        return(False, None)

def vraagloop(prompt):
    vervolg = False
    while vervolg == False:
        x = input(prompt + " ")
        vervolg, awoord = antwoord(x)
    return awoord

def winst(data, dier, plaats):
    vraag = f'Is het dier een {dier}?'
    x = vraagloop(vraag)
    if x == True:
        print('hee gewonnen, lekker hoor....')
        restart()
    else:
        save_the_animal(data, dier, plaats)

def vraag1(data):
    awoord = vraagloop(data['vraag'])
    if awoord == True:
        if isinstance(data['ja'], dict):
            vraag1(data['ja'])
        else:
            winst(data, data['ja'], 'ja')        
    if awoord == False:
        if isinstance(data['nee'], dict):
            vraag1(data['nee'])
        else: 
            winst(data, data['nee'], 'nee')

def save_and_quit(dieren):
    dieren = removestuff(dieren)
    y = json.dumps(dieren)
    f = open('database.txt', 'w')
    f.write(y)
    f.close()
    print('Bedankt voor het spelen en tot ziens!')
    quit()

        
# functies om vragen aan te passen
def vraagcheck(x, len):
    try:
        y = int(x)
    except:
        return False
    if y > len or y < 1:
        return False
    else: return True

def showvraag(lisso, inc= 0):
    for i in lisso:
        inc +=1
        print(str(inc)+".", i)
    x = input('Welke vraag wil je wijzigen: ')
    y = vraagcheck(x, len(lisso))
    if y == True:
        return int(x)-1
    else: 
        time.sleep(1)
        print("\n" + random.choice(['Hier gaat iets fout...', "Dit willen we niet...", "Nee, nee... "]))
        return showvraag(lisso)

def schrijfvraag(index, lijstmetvragen):
    vraag = input(f'Je hebt gekozen om de vraag: "{lijstmetvragen[index]}" te wijzigen. \nSchrijf hier de nieuwe vraag: ').strip().capitalize()
    if vraag.endswith('?') == False: vraag += "?"
    print(vraag)
    if vraagloop('Ben je tevreden met de vraag? '):
        print(random.choice(['Toppie', 'Mooi man', 'Chill', 'Lekker chica']))
        return lijstmetvragen[index], vraag
    else: 
        schrijfvraag(index, lijstmetvragen)

def updatedicto(Ovraag, Nvraag, dieren):
    if isinstance(dieren, dict):
        for k,v in dieren.items():
            if k == 'vraag':
                if dieren['vraag'] == Ovraag:
                    dieren['vraag'] = Nvraag   
                    break        
            else: updatedicto(Ovraag, Nvraag, v)

def updatevraag(dieren):
    lijstmetvragen = vraag(dieren)
    indexvraag = showvraag(lijstmetvragen)
    Ovraag, Nvraag = schrijfvraag(indexvraag, lijstmetvragen)
    updatedicto(Ovraag, Nvraag, dieren)
    restart()

def vraag(dieren, lisso=None):
    if lisso == None: lisso = []
    if isinstance(dieren, dict):
        for k,v in dieren.items():
            if k == 'vraag':
                lisso.append(v)
            else: vraag(v, lisso)
    return lisso

def lijstmetdieren(dieren, lisso = None):
    if lisso == None: lisso = []
    if isinstance(dieren, dict):
        for k,v in dieren.items():
            if isinstance(v, str):
                lisso.append(v)
            else: lijstmetdieren(v, lisso)
    lisso = [x for x in lisso if len(x.split()) == 1]
    lisso.sort()
    return lisso
    
#Restart functie
def restart():
    x = 'Wil je opnieuw spelen? '
    y = vraagloop(x)
    if y == True:
        start(dieren)
    if y == False:
        z = vraagloop('Wil je één van de vragen aanpassen? ')
        if z == True:
            updatevraag(dieren)
        else:
            w = vraagloop('Wil je de lijst met alle dieren zien? ')
            if w == True:
                print(lijstmetdieren(dieren))
                restart()
            else:
                save_and_quit(dieren)

def begin(dieren):
    dieren = addstuff(dieren)
    start(dieren)

begin(dieren)