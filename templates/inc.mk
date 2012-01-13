# course information
CODE?=DT001G
NAME?=itgru
TEXDIRS?=inl-1_3 inl-2_5 inl-2_6 inl-3_1 inl-3_2 inl-3_3
LABDIRS?=

MKDIR?=/bin/mkdir
CP?=/bin/cp
MAKE?=/usr/bin/make
EDITOR?=/usr/bin/vim
GREP?=/bin/grep
WGET?=/usr/bin/wget
SED?=/bin/sed
XARGS?=/usr/bin/xargs
WWW?=/usr/bin/firefox

kursplan:
	@wget -o /dev/null -O - \
	"http://www.miun.se/sv/Utbildning/Hitta-din-utbildning/Kurser/Sok-kursplan/?code=${CODE}&show=1&sort=KursBenamning&dosearch=true" \
	| ${SED} -n 's/<a .*href="\([^"]*\)".*>${CODE}<\/a>/http:\/\/www.miun.se\1/p' \
	| ${XARGS} ${WWW}
