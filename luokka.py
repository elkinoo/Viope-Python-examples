# Määritellään luokkaa nimeltä Kilpailija, jolle annettaan kaksi jäsenmuuttujaa, pisteet ja vari. Tämän jälkeen luo luokasta olio "eka", jolle annetaan muuttujan vari arvoksi sininen ja pisteet arvoksi 10. Lopuksi laita ohjelmasi vielä tulostamaan olion tiedot muodossa "Kilpailijalla [väri] on [pisteet] pistettä!"

class Kilpailija:
	eka = "sininen"
	pisteet = 10
	
kilpailija = Kilpailija()

kilpailija.eka = "sininen"
kilpailija.pisteet = 10
	
print ("Kilpailijalla "+kilpailija.eka+" on "+str (kilpailija.pisteet)+" pistettä!")