CATEGORY=	itgrund/workshops
FILES= 		latex.tex literature.bib
FILES+= 	dokument.tex
DOCUMENTS=	latex.pdf dokument.pdf

PACKAGE=		latex-src
TARBALL_FILES=	${FILES} Makefile

PUB_FILES=	${PACKAGE}.tar.gz ${DOCUMENTS}

latex.pdf: ${FILES}
dokument.pdf: dokument.tex literature.bib

#export no
literature.bib: ../../literature.bib
	${CP} $^ $@
Makefile.export: Makefile

TARBALL_FILES= 	${FILES:.tex=.exporttex} Makefile.export

clean:
	${RM} literature.bib
#endexport

miun.depend.mk:
	wget http://ver.miun.se/build/$@

include miun.depend.mk
include miun.course.mk
include miun.package.mk
