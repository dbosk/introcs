#encoding: utf8

# en lista att spara kommandohistoriken i.
history = []

# vår dictionary som håller koll på var programmet
# finns för att köra ett visst kommando.
cmds = {
	"ls" : "/usr/bin/ls",
	"cp" : "/usr/bin/cp",
	"mv" : "/usr/bin/mv",
	"res" : "/usr/local/bin/res",
	"course" : "/usr/local/bin/course",
	"python" : "/opt/sfw/bin/python",
	"emacs" : "/usr/local/bin/emacs",
	"vim" : "/opt/sfw/bin/vim",
	"g++" : "/usr/sfw/bin/g++",
	"cc" : "/usr/local/bin/cc",
	"gdb" : "/opt/sfw/bin/gdb"
	}

cmd = input( "Enter command: " )
while cmd != "exit":
	try:
		print( cmds[cmd] )
		# koden nedan kommer aldrig inträffa om det blir
		# en exception i cmds[cmd], då hoppar den direkt
		# till except nedan.
		history.append( cmd )

	except KeyError:
		print( "Sorry, that command is not in the dictionary." )
	except:
		print( "There is something seriously wrong here." )

	cmd = input("Enter command: ")

for cmd in history:
	print( cmd, end = "\n" )

try:
	histfile = open( "history", "w" )
except:
	print( "Couldn't open file for writing." )
else:
	for cmd in history:
		histfile.write( cmd + "\n" )

