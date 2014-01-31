# $Id$

DOCUMENTS=	report.pdf
FILES=		report.tex literature.bib rfc.bib
FILES+=		abstract.tex
FILES+=		intro.tex theory.tex method.tex results.tex discussion.tex
FILES+=		data.tex
CATEGORY=	itgrund/project
PACKAGE=	report-src
PACKAGE_FILES=	${FILES} Makefile
PUB_FILES=	${DOCUMENTS} ${PACKAGE}.tar.gz

USE_LATEXMK= 	yes
USE_BIBLATEX= 	yes

report.pdf: ${FILES}

#export no

Makefile.export: Makefile
PACKAGE_FILES=	${FILES:.tex=.exporttex} Makefile.export

literature.bib: ../../literature.bib
	${CP} $^ $@

clean:
	${RM} literature.bib

#endexport

### INCLUDES ###

miun.depend.mk:
	wget http://ver.miun.se/build/$@

include miun.depend.mk
include miun.course.mk
include miun.package.mk
