#Tässä tehtävässä laajennetaan ensimmäistä tehtävää, ja otetaan mukaan toinen luku. Jos yksi käyttäjän syöttämistä luvuista on parillinen, tulostetaan "Toinen luku on parillinen", jos molemmat niin "Molemmat luvut on parillisia." Mikäli kumpikaan käyttäjän antama luku ei ole parillinen, tulostetaan "Molemmat luvut ovat parittomia." 

eka = int(input("Anna luku: "))
toka = int(input("Anna toinen luku: "))

	
if (eka % 2 == 0) and (toka % 2 ==0):
	print ("Molemmat luvut ovat parillisia.")

elif (eka % 2 == 0) or (toka % 2 == 0):
	print ("Toinen luku on parillinen.")
	
else:
	print ("Molemmat luvut ovat parittomia.")