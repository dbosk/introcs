#encoding: iso-8859-1
# importera random-biblioteket
import random

# Skriv en välkomsttext.
print "Välkommen till prov i matematik!"

x = 0		# håll koll på antalet frågor
korrekt = 0	# håll koll på antalet korrekta svar

# provet innehåller 10 frågor, så "snurra" 10 varv.
while x < 10:
	# skapa två slumpade heltal mellan 0 och 10.
	tal1 = random.randint(0,10)
	tal2 = random.randint(0,10)

	print tal1, "+", tal2, "=",
	# ta ett svar som text från tangentbordet ...
	svar = raw_input()
	# ... och gör om det till ett heltal
	svar = int(svar)

	# kolla om svaret är korrekt
	if svar == tal1+tal2:
		print "Korrekt"
		# detta var ett korrekt svar, ökat antalet sådana med ett.
		korrekt = korrekt + 1
	else:
		print "Fel"
	
	# nu har vi klarat av ytterligare en fråga.
	x = x + 1

# skriv ut lite statistik till användaren
print "Du hade", korrekt, "korrekta svar av", x, "möjliga!"
# gör om till flyttal (decimaltal) och dela med det hela, dvs räkna ut
# procenten. det krävs 50% för godkänt.
if float(korrekt)/x > 0.5:
	print "Grattis, du är godkänd!"

raw_input("Tryck en tangent för avslut ...")
