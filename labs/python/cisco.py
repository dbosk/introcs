#encoding: utf8

import random

questions = [ ["Vad heter Ciscos VD?", "Urban Turban"],
		["Hur många portar med terabitstöd har en Cisco X500 SuperPro GrooveRoute?", "1/2"] ]

def ask_question( questions ):
	q = random.choice( questions )
	answer = input( q[0] + "\n" )
	if ( answer == q[1] ):
		return 1
	return 0


##################
# Huvudprogrammet
##################

question_count = 0
correct_count = 0

keep_running = "ja"

# the main loop: this is where we pose all questions to the user
while ( keep_running == "ja" ):
	correct_count += ask_question( questions )
	question_count += 1

	keep_running = ""
	while ( keep_running != "ja" and keep_running != "nej" ):
		keep_running = input( "Vill du fortsätta? (ja/nej) " )

# now we're done, the user chose to quit, calculate scores
result = 100 * float( correct_count ) / question_count

print( "Du fick totalt " + str( result ) + "% rätt." )

# decide if the user passed or failed
if ( result >= 70 ):
	print( "Du blev godkänd, grattis!" )
else:
	print( "Det gick ju mindre bra, du skulle ha valt att köra igen." )

