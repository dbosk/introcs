CATEGORY=	itgrund/labs
FILES=		terminal.tex aims.tex literature.tex literature.bib
DOCUMENTS=	terminal.pdf

PACKAGE=		terminal-src
TARBALL_FILES=	${FILES}

PUB_FILES=		${DOCUMENTS} ${PACKAGE}.tar.gz

USE_LATEXMK= 	yes
USE_BIBLATEX= 	yes

terminal.pdf terminal.ps: ${FILES}

#export no
literature.bib: ../../literature.bib
	${CP} $^ $@
Makefile.export: Makefile

TARBALL_FILES= 	${FILES:.tex=.exporttex} Makefile.export

clean:
	${RM} literature.bib
#endexport

miun.depend.mk:
ifeq (${MAKE},gmake)
	lynx -dump http://ver.miun.se/build/$@ > $@
else
	wget http://ver.miun.se/build/$@
endif

include miun.depend.mk
include miun.course.mk
include miun.package.mk
