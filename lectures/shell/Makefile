CATEGORY=	itgrund/lectures
FILES=		shell.tex literature.bib
DOCUMENTS=	shell.pdf

PACKAGE=		shell-src
TARBALL_FILES=	${FILES} Makefile

PUB_FILES=	${PACKAGE}.tar.gz ${DOCUMENTS}

shell.pdf: ${FILES}

#export no
literature.bib: ../../literature.bib
	${CP} $^ $@

TARBALL_FILES= 	Makefile.export ${FILES:.tex=.exporttex}

Makefile.export: Makefile
#endexport

miun.depend.mk:
	wget http://ver.miun.se/build/$@

include miun.depend.mk
include miun.course.mk
include miun.package.mk
