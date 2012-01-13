PUBDIR=

publish-all: ${FILES}
	@${CP} ${FILES} ${PUBDIR}

publish: ${FILE}
	@${CP} ${FILE} ${PUBDIR}
