CATEGORY=	itgrund/labs
FILES=		python.tex aims.tex literature.tex literature.bib
DOCUMENTS=	python.pdf

PACKAGE=		python-src
TARBALL_FILES=	${FILES}

PUB_FILES=		${PACKAGE}.tar.gz ${DOCUMENTS}

python.pdf python.ps: ${FILES}

USE_LATEXMK= 	yes
USE_BIBLATEX= 	yes

#export no

TARBALL_FILES= 	${FILES:.tex=.exporttex} Makefile.export

Makefile.export: Makefile
literature.bib: ../../literature.bib
	${CP} $^ $@

clean:
	${RM} literature.bib

#endexport

miun.depend.mk:
	wget http://ver.miun.se/build/$@

include miun.depend.mk
include miun.course.mk
include miun.package.mk
