#maak een nieuwe lijst
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#lijst = []

#for number in a:
 # if number <= 5:
  #  lijst.append(number)
#print(lijst)

# code kleiner maken 
#b= [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#even_lijst = [even for even in b if even %2 == 0 ]
#print(even_lijst)

# guess the number
import random
random_number = random.randint(1,9)
nummer_gevonden = False
aantal_pogingen = 0

while nummer_gevonden == False:
  raad = int(input("kies een nummer tussen 1 en 9: "))
  
  aantal_pogingen = aantal_pogingen + 1
  if raad == random_number:
    nummer_gevonden = True
    print(f"het nummmer is geraden in {aantal_pogingen} keer")
  elif raad < random_number:
    nummer_gevonden = False
    print("te laag")
  else:
    nummer_gevonden = False
    print("te hoog")


