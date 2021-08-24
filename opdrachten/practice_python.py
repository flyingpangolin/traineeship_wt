# oefenen met een functie
# maak een lijst met de 1ste en laatse elementen van de oude lijst
a = [1,2,3,4,5,6,7]
b = [ 3, 6, 10, 12]

def verkleinen(een_lijst):
    return [een_lijst[0], een_lijst[len(een_lijst)-1]] 

print(verkleinen(a))
print(verkleinen(b))

# verwijder dubbelen (maak van een lijst een set)
c = [1,1,2,2,3,3,4,4]

def verwijder(x):
    return list(set(x))

print(verwijder(c))

#opdracht 15
s = "het is warm vandaag"  
def reverse_v4(w):
  y = w.split()
  y.reverse()
  return " ".join(y)

print(reverse_v4(s))

#wachtwoord generator 
import random
opties = "1234567890!@#$%^&*()?QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"


input("wil je een nieuw wachtwoord, ja of nee? ")
if "ja":
    passlen = int(input("geef het aantal tekens van je gewenste wachtwoord. "))
    wachtwoord = random.sample(opties,passlen)
    print("". join (wachtwoord))
else:
    print("oke")





