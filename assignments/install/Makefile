CATEGORY=	itgrund/assignments
FILES=		install.tex literature.tex literature.bib
DOCUMENTS=	install.pdf

PACKAGE=		install-src
PACKAGE_FILES=	${FILES}

PUB_FILES=		${PACKAGE}.tar.gz ${DOCUMENTS}

install.pdf: install.tex literature.tex literature.bib
literature.bib: ../../literature.bib
	${CP} $^ $@

clean:
	${RM} literature.bib

include miun.course.mk
include miun.package.mk
