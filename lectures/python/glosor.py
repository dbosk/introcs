#encoding: latin1
# behöver slumpfunktioner
import random

# glosa nr:  0          1             2
sprak1 = ["mjölk", "köttfärssås", "katastrof"]
# översättningar
sprak2 = ["milk", "meat sauce", "catastrophy"]

# hur många glosor ska vi förhöra?
antal_glosor = 5
# hur många rätt har vi hittills?
antal_ratt = 0

# håll koll på hur många glosfrågor vi ställt. börja med 0.
fraga = 0
# så länge vi ställt färre frågor än antal_glosor ...
while fraga < antal_glosor:
	# ... så ska vi göra allt som är inhoppat
	# välj ett slumpmässigt glosnummer
	glosnr = random.randint(0, len(sprak1)-1)
	# fråga användaren ...
	print "vad är", sprak1[glosnr], "?"
	svar = raw_input()
	# ... och kontrollera svaret.
	if svar == sprak2[glosnr]:
		print "Korrekt"
		# vi fick ett till rätt svar, uppdatera antal_ratt.
		antal_ratt = antal_ratt + 1
	else:
		print "Fel, det är", sprak2[glosnr]

	# nu är vi färdiga med ytterligare en fråga. uppdatera vilken fråga vi är
	# på.
	fraga = fraga + 1


raw_input("Tryck en tanget för avslut ...")
