#encoding: utf8

import sys

def Mbps2Mibps( speed ):
	# 1 Mbit/s = 1000 kbit/s = 1000000 bit/s
	# 1 Mibit/s = 1024 Kibit/s = 1024^2 bit/s = 1048576 bit/s
	return speed * ( 1000000 / float(1048576) )

# konverteringsfunktioner till och från bit/s för olika storhetsprefix
def Gbps2bps( speed ):
	return speed * 1000000000

def bps2Gbps( speed ):
	return float( speed ) / 1000000000

def Mbps2bps( speed ):
	return speed * 1000000

def bps2Mbps( speed ):
	return float( speed ) / 1000000

def kbps2bps( speed ):
	return speed * 1000

def bps2kbps( speed ):
	return float( speed ) / 1000

def Mibps2bps( speed ):
	return speed * 1048576

def bps2Mibps( speed ):
	return float( speed ) / ( 1024*1024 )

def kibps2bps( speed ):
	return speed * 1024

def bps2kibps( speed ):
	return float( speed ) / 1024

# returnera antalet bytes (utan enhetsprefix)
def parse_data( s ):
	# 1 MB = 1000 kB = 1000000 B
	# 1 MiB = 1024 KiB = 1024^2 B = 1048576 B
	s = s.split() # "123 m" -> ["123", "m"]
	data = float( s[0] )
	# kontrollera att listan faktiskt innehåller två element
	if ( len( s ) < 2 ):
		raise Exception( "Enhetsprefix saknas" )
	prefix = s[1]

	# kolla enhetsprefix och multiplicera med lämpligt tal
	if ( prefix == "k" ):
		#data = data * 1000
		data *= 1000
	elif ( prefix == "Ki" ):
		data *= 1024
	elif ( prefix == "M" ):
		data *= 1000*1000
	elif ( prefix == "m" ):
		# för millibytes
		data /= 1000
	elif ( prefix == "Mi" ):
		data *= 1024*1024
	elif ( prefix == "G" ):
		data *= 1000*1000*1000
	elif ( prefix == "Gi" ):
		data *= 1024**3
	elif ( prefix == "T" ):
		data *= 1000**4
	elif ( prefix == "Ti" ):
		data *= 1024**4
	else:
		# ge ett särfall med tillhörande felmeddelande
		raise Exception( "Enhetsprefix '" + prefix + "' finns inte" )

	return data

# returnera tiden i sekunder
def parse_time( s ):
	s = s.split()
	time = float( s[0] )
	# kontrollera att listan faktiskt innehåller två element
	if ( len( s ) < 2 ):
		raise Exception( "Tidsenhet saknas" )
	# ta ut tidsenheten
	unit = s[1]

	# undersök vilken tidsenhet som användaren vill ha
	if ( unit == "min" ):
		time *= 60
	elif ( unit == "h" ):
		time *= 60*60
	elif ( unit == "d" ):
		time *= 24*60*60
	elif ( unit == "y" ):
		time *= 365*24*60*60
	# men enbart "s" är SI-enhet, så undvik "sek"
	elif ( unit == "s" or unit == "sek" ):
		time *= 1
	else:
		# ge ett särfall med tillhörande felmeddelande
		raise Exception( "Tidsenheten '" + unit + "' finns inte" )

	return time

# gör om huvudprogrammet till en separat funktion för att underlätta
# för while-slingan (mindre kod där, mer modulär kod generellt också).
# funktionen tar ett argument logfile som är en öppen fil som vi kan
# skriva loggen till.
def interactive_convert( logfile ):
	# använd raw_input för python2 och input för python3
	data = ""
	while ( data == "" ):
		data = input("Ange datamängd i bytes (ange enhetsprefix efter" \
				"mellanslag, 0 för avslut): ")
	if ( data == "0" ):
		# alternativt sys.exit( 0 ), båda fungerar
		return True
	# skriv till loggen
	logfile.write( data + "\n" )
	try:
		data = parse_data( data )
	except Exception as e:
		print( e )
		sys.exit( 1 )

	print( "Datamängden är " + str( data ) + " bytes." )
	logfile.write( str( data ) + " bytes\n" )

	# använd raw_input för python2 och input för python3
	time = input("Ange tid (enhet efter mellanslag): ")
	logfile.write( time + "\n" )
	try:
		time = parse_time( time )
	except Exception as ex:
		print( ex )
		sys.exit( 1 )

	print( "Tiden är " + str( time ) + " sekunder." )
	logfile.write( str( time ) + " sekunder\n" )

	# vill ha hastigheten i bit/s (8 bitar per byte)
	speed = 8 * data / time
	logfile.write( str( speed ) + " bit/s\n" )

	print( "Det ger en hastighet på ")

	# vi behöver en logfile.write för varje sak vi vill skriva till loggen,
	# många blir det.  för att underlätta skapar vi en ny variabel newspeed
	# som kan agera mellanlagring.
	newspeed = ""
	if ( speed > 1000000000 ):
		newspeed = str( bps2Gbps( speed ) ) + " Gbit/s"
	elif ( speed > 1000000 ):
		newspeed = str( bps2Mbps( speed ) ) + " Mbit/s"
	elif ( speed > 1000 ):
		newspeed = str( bps2kbps( speed ) ) + " kbit/s"
	else:
		newspeed = str( speed ) + " bit/s"
	
	print( newspeed )
	logfile.write( newspeed + "\n" )

	return False 

#############################
# Huvudprogrammet börjar nu här
#############################

# försök att öppna loggfilen för skrivning
try:
	logfile = open( "convert.log", "w" )
# meddela eventuella fel och avsluta
except Exception as e:
	print( e )
	sys.exit( 1 )

# kör konverteringen så länge användaren inte vill avsluta
quit = False
while ( not quit ):
	# vi skickar med loggfilen och får tillbaka om användaren vill
	# avsluta eller ej
	quit = interactive_convert( logfile )

# glöm inte att stänga loggfilen
logfile.close()
