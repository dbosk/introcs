#encoding: latin1
# beh�ver slumpfunktioner
import random

# glosa nr:  0          1             2
sprak1 = ["mj�lk", "k�ttf�rss�s", "katastrof"]
# �vers�ttningar
sprak2 = ["milk", "meat sauce", "catastrophy"]

# hur m�nga glosor ska vi f�rh�ra?
antal_glosor = 5
# hur m�nga r�tt har vi hittills?
antal_ratt = 0

# h�ll koll p� hur m�nga glosfr�gor vi st�llt. b�rja med 0.
fraga = 0
# s� l�nge vi st�llt f�rre fr�gor �n antal_glosor ...
while fraga < antal_glosor:
	# ... s� ska vi g�ra allt som �r inhoppat
	# v�lj ett slumpm�ssigt glosnummer
	glosnr = random.randint(0, len(sprak1)-1)
	# fr�ga anv�ndaren ...
	print "vad �r", sprak1[glosnr], "?"
	svar = raw_input()
	# ... och kontrollera svaret.
	if svar == sprak2[glosnr]:
		print "Korrekt"
		# vi fick ett till r�tt svar, uppdatera antal_ratt.
		antal_ratt = antal_ratt + 1
	else:
		print "Fel, det �r", sprak2[glosnr]

	# nu �r vi f�rdiga med ytterligare en fr�ga. uppdatera vilken fr�ga vi �r
	# p�.
	fraga = fraga + 1


raw_input("Tryck en tanget f�r avslut ...")
