CATEGORY=	itgrund/lectures
FILES=		intro.tex literature.bib
DOCUMENTS=	intro.pdf

PACKAGE= 		intro-src
TARBALL_FILES= 	Makefile ${FILES}

USE_LATEXMK= 	yes
USE_BIBLATEX= 	yes

intro.pdf intro.ps: ${FILES}

#export no

TARBALL_FILES= 	Makefile.export ${FILES:.tex=.exporttex}
PUB_FILES= 		${PACKAGE}.tar.gz ${DOCUMENTS}

literature.bib: ../../literature.bib
	${CP} $^ $@

clean:
	${RM} ${DOCUMENTS} literature.bib

#endexport

miun.depend.mk:
ifeq (${MAKE},gmake)
	lynx -dump http://ver.miun.se/build/$@ > $@
else
	wget http://ver.miun.se/build/$@
endif

include miun.depend.mk
include miun.course.mk
