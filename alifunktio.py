#Tee tehtävä, jossa on pääfunktio main ja alifunktio "toinenpotenssi". Alifunktio ottaa vastaan yhden parametrin, laskee sille toisen potenssin ja tulostaa vastauksen muodossa "Toinen potenssi on [vastaus]". Pääohjelma vastaavasti pyytää käyttäjältä lukua "Anna lukuarvo: " ja lähettää sen eteenpäin alifunktiolle.
def main():

	lukuq = int(input("Anna lukuarvo: "))

	def potenssi(luku):
		print("Toinen potenssi on "+str(+luku**2))
	
	potenssi(lukuq)

main()