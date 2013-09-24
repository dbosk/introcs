#encoding: utf8

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

data = float( input("Ange datamängd (megabyte): ") )
time = float( input("Ange tid (minuter): ") )

# vill ha hastigheten i Mbit/s (8 bitar per byte)
speed = 8 * data / ( time * 60 )

print( "Det ger en hastighet på ")

newspeed = Mbps2bps( speed )
if ( newspeed > 1000000000 ):
	print( str( bps2Gbps( newspeed ) ) + " Gbit/s" )
elif ( newspeed > 1000000 ):
	print( str( bps2Mbps( newspeed ) ) + " Mbit/s" )
elif ( newspeed > 1000 ):
	print( str( bps2kbps( newspeed ) ) + " kbit/s" )
else:
	print( str( newspeed ) + " bit/s" )

#print( "Det ger en hastighet på " + str( speed ) + " Mbit/s" )
#print( "Alternativt " + str( bps2kibps(Mbps2bps( speed )) ) + " kibit/s" )
