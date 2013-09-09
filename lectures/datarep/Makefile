CATEGORY=	itgrund/lectures
FILES=		datarep.tex literature.bib
DOCUMENTS=	datarep.pdf

PACKAGE= 		datarep-src
TARBALL_FILES= 	${FILES} Makefile

datarep.pdf: ${FILES}

#export no
literature.bib: ../../literature.bib
	${CP} $^ $@
Makefile.export: Makefile

TARBALL_FILES= 	${FILES:.tex=.exporttex} Makefile.export
PUB_FILES= 		${PACKAGE}.tar.gz ${DOCUMENTS}
#endexport

miun.depend.mk:
	wget http://ver.miun.se/build/$@

include miun.depend.mk
include miun.course.mk
include miun.package.mk
