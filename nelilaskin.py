# Laajenna aiemmin aloittamaasi laskinta siten, että if-valintarakenteen avulla on mahdollista valita tehdäänkö luvuille yhteen- (valinta 1), vähennys- (valinta 2), kerto- (valinta 3) vai jakolasku (valinta 4). Lisäksi lisää ohjelman alkuun käyttäjälle ohje siitä, mitä eri valinnat tekevät, sekä ohjelmaan toiminto, millä ohjelma tulostaa "Valintaa ei tunnistettu", mikäli käyttäjä valitsee jotain muuta kuin valinnan väliltä 1-4. Tämä on helpointa toteuttaa else-osion avulla.
eka = int(input("Anna ensimmäinen luku: "))
toka = int(input("Anna toinen luku: "))

print ("(1) +")
print ("(2) -")
print ("(3) *")
print ("(4) /")

kohde = int(input("Tee valinta (1-4): "))

if kohde == 1:
	print ("Tulos on: "+str(eka+toka))
	
elif kohde == 2:
	print ("Tulos on: "+ str(eka-toka))
	
elif kohde == 3:
	print ("Tulos on: " + str(eka*toka))

elif kohde == 4:
	print ("Tulos on: "+ str(eka/toka))
	
else:
	print ("Valintaa ei tunnistettu.")	