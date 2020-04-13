# Tee virheenkorjausrakenne, jossa käyttäjältä pyydetään luku "Anna luku: ", ja mikäli tyyppimuunnos onnistuu, tulostetaan "Syöte oli kelvollinen." ja virheen tapahtuessa "Virheellinen syöte!"
luku = input("Anna luku: ")

try:
	luku = int(luku)
	print("Syöte oli kelvollinen.")
	
except Exception:
	print("Virheellinen syöte!")