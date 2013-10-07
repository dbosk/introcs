#encoding: latin1
########################################
# Funktioner
########################################

# en funktion som ritar en b tecken bred linje på skärmen
def linje(b):
	# "snurra" i loopen b varv, skriv ut ett # varje varv.
	for x in range(b):
		print '#',
	print

# en funktion som ritar en b tecken bred och h tecken hög rektangel på skärmen
def rektangel(h,b):
	# "snurra" i loopen h varv, skriv ut en linje av bredden b varje varv.
	for y in range(h):
		linje(b)

# funktionen räknar ut arean för en rektangel med höjden h och basen b
def area(h, b):
	# returnera basen gånger höjden
	return h*b



########################################
# Huvudprogram
########################################

svar = raw_input('Hur bred ska linjen vara?')
lbredd = int(svar)

rbredd = int(raw_input('Hur bred ska rektangeln vara?'))
rhojd = int(raw_input('Hur hög ska rektangeln vara?'))

linje(lbredd)
rektangel(rhojd, rbredd)

print "Arean är", area(rhojd, rbredd),"kvadrattecken"

raw_input("Tryck en tangent för avslut ...")
