PUBDIR=/afs/.nada.kth.se/misc/info/DD1314/www-csc/prgmed09/O/grp3

publish-all: ${FILES}
	@${CP} ${FILES} ${PUBDIR}

publish: ${FILE}
	@${CP} ${FILE} ${PUBDIR}
