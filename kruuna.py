#Tee ohjelma, joka arpoo viisi kertaa joko luvun 0 tai 1 käyttäen random.randint-kirjastofunktiota. Mikäli ohjelma arpoo luvun 0, tulostetaan "Klaava!", mikäli 1 niin "Kruuna!". Ohjelma alkaa tulosteella "Heitetään kolikkoa viidesti:"

import random
print ("Heitetään kolikkoa viidesti:")


for i in range(5):
	luku = random.randint(0,1)	
	if luku == 0:
		print ("Klaava!")
		
	else:
		print ("Kruuna!")