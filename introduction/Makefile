CATEGORY=	itgrund
FILES=		literature.tex ../literature.bib welcome.tex \
			kursplan.pdf
DOCUMENTS=	literature.pdf welcome.pdf

PACKAGE=		intro-src
PACKAGE_FILES=	${FILES}

PUB_FILES=		${PACKAGE}.tar.gz ${DOCUMENTS}

literature.pdf: literature.tex ../literature.bib rfc.bib \
	../assignments/install/literature.tex \
	../assignments/terminal/literature.tex \
	../assignments/latex/literature.tex \
	../assignments/computer/literature.tex \
	../assignments/internet/literature.tex \
	../assignments/security/literature.tex \
	../assignments/sftp/literature.tex
welcome.pdf: welcome.tex kursplan.pdf
studyguide.pdf: studyguide.tex ../literature.bib

include miun.course.mk
include miun.package.mk
