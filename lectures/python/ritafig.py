#encoding: latin1
########################################
# Funktioner
########################################

# en funktion som ritar en b tecken bred linje p� sk�rmen
def linje(b):
	# "snurra" i loopen b varv, skriv ut ett # varje varv.
	for x in range(b):
		print '#',
	print

# en funktion som ritar en b tecken bred och h tecken h�g rektangel p� sk�rmen
def rektangel(h,b):
	# "snurra" i loopen h varv, skriv ut en linje av bredden b varje varv.
	for y in range(h):
		linje(b)

# funktionen r�knar ut arean f�r en rektangel med h�jden h och basen b
def area(h, b):
	# returnera basen g�nger h�jden
	return h*b



########################################
# Huvudprogram
########################################

svar = raw_input('Hur bred ska linjen vara?')
lbredd = int(svar)

rbredd = int(raw_input('Hur bred ska rektangeln vara?'))
rhojd = int(raw_input('Hur h�g ska rektangeln vara?'))

linje(lbredd)
rektangel(rhojd, rbredd)

print "Arean �r", area(rhojd, rbredd),"kvadrattecken"

raw_input("Tryck en tangent f�r avslut ...")
