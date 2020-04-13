#Toteuta ohjelma, joka joka kierroksen alussa pyytää käyttäjältä merkkijonon ja tulostaa sen ruudulle. Ainoan poikkeuksen tähän tekee tilanne, jossa käyttäjä kirjoittaa tekstin "lopeta", jolloin ohjelma tulostaa tekstin "Lopetit ohjelman" ja sammuu.

while True:
	jono = str(input("Kirjoita jotain: "))	
	  if jono == "lopeta":
		  print("Lopetit ohjelman.")
	  	break
	  else:
		print(jono)