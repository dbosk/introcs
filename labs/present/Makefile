CATEGORY=	itgrund/labs
FILES=		present.tex literature.bib literature.tex
DOCUMENTS=	present.pdf

USE_LATEXMK= 	yes
USE_BIBLATEX= 	yes

present.pdf: ${FILES}

#export no
TARBALL_FILES= 	${FILES} Makefile.export
PUB_FILES= 		${PACKAGE}.tar.gz ${DOCUMENTS}

literature.bib: ../../literature.bib

literature.bib:
	${CP} $^ $@

clean:
	${RM} literature.bib
#endexport

miun.depend.mk:
	wget http://ver.miun.se/build/$@

include miun.depend.mk
include miun.course.mk
