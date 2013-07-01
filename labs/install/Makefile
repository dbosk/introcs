CATEGORY=	itgrund/labs
FILES=		install.tex literature.tex literature.bib
DOCUMENTS=	install.pdf

PACKAGE=		install-src
PACKAGE_FILES=	${FILES}

PUB_FILES=		${PACKAGE}.tar.gz ${DOCUMENTS}

install.pdf install.ps: ${FILES}

USE_LATEXMK= 	yes
USE_BIBLATEX= 	yes

#export no

PACKAGE_FILES= 	${FILES:.tex=.exporttex} Makefile.export

literature.bib: ../../literature.bib
	${CP} $^ $@

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
