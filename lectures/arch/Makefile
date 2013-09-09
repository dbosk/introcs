CATEGORY=	itgrund/lectures
FILES=		arch.tex literature.bib
DOCUMENTS=	arch.pdf

PACKAGE= 		arch-src
TARBALL_FILES= 	${FILES} Makefile

arch.pdf: ${FILES}

#export no
literature.bib: ../../literature.bib
	${CP} $^ $@
Makefile.export: Makefile

TARBALL_FILES= 	${FILES:.tex=.exporttex} Makefile.export
PUB_FILES= 		${PACKAGE}.tar.gz ${DOCUMENTS}

clean:
	${RM} literature.bib
#endexport

miun.depend.mk:
	wget http://ver.miun.se/build/$@

include miun.depend.mk
include miun.course.mk
include miun.package.mk
