CATEGORY=	itgrund/assignments
FILES=		terminal.tex literature.tex literature.bib
DOCUMENTS=	terminal.pdf

PACKAGE=		terminal-src
PACKAGE_FILES=	${FILES}

PUB_FILES=		${DOCUMENTS}

USE_LATEXMK= 	yes
USE_BIBLATEX= 	yes

terminal.pdf: ${FILES}
literature.bib: ../../literature.bib
	${CP} $^ $@

clean:
	${RM} literature.bib

include miun.course.mk
include miun.package.mk
