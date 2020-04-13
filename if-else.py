# Ohjelmassa käyttäjältä pyydetään nimi ja salasana. Jos nimi on väärin, tulostaa ohjelma "Nimi oli väärin.". Jos nimi on oikein, pyydetään salasanaa. Jos salasana on oikein, tulostetaan "Salasana ja nimi oli oikein!", muussa tapauksessa "Salasana oli väärin.". Toteuta oikeaksi nimi-salasana-pariksi Erkki ja Esimerkki. 

nimi = str(input("Anna nimi: "))
if nimi == "Erkki":
	salasana = str(input("Anna salasana: "))	
	if salasana == "Esimerkki":
		print("Salasana ja nimi oli oikein!")
	else:
		print("Salasana oli väärin.")
else:
	print("Nimi oli väärin.")