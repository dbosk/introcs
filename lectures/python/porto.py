#encoding: utf8

# weight är vikten, i gram, hos ett brev.
# rätt porto returneras.
def check_postage( weight ):
	## POSTENS 1:a KLASS INRIKES BREV
	if ( weight <= 20 ):
		return 6
	elif ( weight <= 100 ):
		return 12
	elif ( weight <= 250 ):
		return 24
	elif ( weight <= 500 ):
		return 36
	elif ( weight <= 1000 ):
		return 48
	elif ( weight <= 2000 ):
		return 72
	## POSTENS POSTPAKET
	elif ( weight <= 3000 ):
		return 150
	elif ( weight <= 5000 ):
		return 175
	elif ( weight <= 10000 ):
		return 225
	elif ( weight <= 15000 ):
		return 275
	elif ( weight <= 20000 ):
		return 320
	return -1


#####################
# Huvudprogrammet
#####################

# Loopa så länge som möjligt
while ( True ):
	print( "Välkommen till Brevvågen" )
	nletters = input( "Hur många brev vill du beräkna porto för (0 " \
		"för att avsluta): " )
	nletters = int( nletters )
	# 0 för att avsluta (negativa också)
	if ( nletters <= 0 ):
		break
	sum = 0
	for i in range( nletters ):
		w = input( "Hur mycket väger brev " + str( i+1 ) + ": " )
		postage = check_postage( float( w ) )
		if ( postage < 0 ):
			print( "Den vikten finns inte med i portotabellen." )
		else:
			print( "Du måste betala", postage, "SEK i porto." )
			sum += postage
	if ( nletters > 1 ):
		print( "Det blir", sum, "SEK för alla brev, tack!" )
	elif ( sum > 100 and nletters == 1 ):
		print( "Mycket pengar för ett postpaket!" )

