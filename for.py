#Tee ohjelma, joka pyytää käyttäjältä kierrosmäärän. Tämän jälkeen tee ohjelma, joka laskee kierroslukujen kertymän. Eli jos käyttäjä antaa syötteen 3, laskee ohjelma 0+1+2, jos 5 niin 0+1+2+3+4. Lopuksi ohjelma tulostaa käyttäjälle lopputuloksen muodossa "Kertymäksi saatiin:" ja vastaus.

kertoma = int(input("Kuinka monta kierrosta?:"))

tulos = int(0)
for kierros in range(0,kertoma):
	tulos = tulos+kierros

print("Kertymäksi saatiin: ",tulos)