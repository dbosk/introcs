#encoding: iso-8859-1
# importera random-biblioteket
import random

# Skriv en v�lkomsttext.
print "V�lkommen till prov i matematik!"

x = 0		# h�ll koll p� antalet fr�gor
korrekt = 0	# h�ll koll p� antalet korrekta svar

# provet inneh�ller 10 fr�gor, s� "snurra" 10 varv.
while x < 10:
	# skapa tv� slumpade heltal mellan 0 och 10.
	tal1 = random.randint(0,10)
	tal2 = random.randint(0,10)

	print tal1, "+", tal2, "=",
	# ta ett svar som text fr�n tangentbordet ...
	svar = raw_input()
	# ... och g�r om det till ett heltal
	svar = int(svar)

	# kolla om svaret �r korrekt
	if svar == tal1+tal2:
		print "Korrekt"
		# detta var ett korrekt svar, �kat antalet s�dana med ett.
		korrekt = korrekt + 1
	else:
		print "Fel"
	
	# nu har vi klarat av ytterligare en fr�ga.
	x = x + 1

# skriv ut lite statistik till anv�ndaren
print "Du hade", korrekt, "korrekta svar av", x, "m�jliga!"
# g�r om till flyttal (decimaltal) och dela med det hela, dvs r�kna ut
# procenten. det kr�vs 50% f�r godk�nt.
if float(korrekt)/x > 0.5:
	print "Grattis, du �r godk�nd!"

raw_input("Tryck en tangent f�r avslut ...")
