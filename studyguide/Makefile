# $Id$

DOCUMENTS=	studyguide.pdf
CATEGORY=	itgrund
FILES=		studyguide.tex literature.bib \
			${LABS} ${SEMINARS} ${PM} ${PROJECT} ${LECTURES}
PACKAGE=	studyguide-src
PACKAGE_FILES=	${FILES} Makefile
PUB_FILES=	${DOCUMENTS} ${PACKAGE}.tar.gz

LABS=		install-aim.tex install-lit.tex
LABS+= 		linux-aim.tex linux-lit.tex
LABS+= 		pylab-aim.tex pylab-lit.tex
LABS+= 		latex-aim.tex latex-lit.tex
#LABS+= 		sftp-aim.tex sftp-lit.tex
SEMINARS=
PM=
PROJECT=	project-aim.tex
LECTURES=	intro-lit.tex
LECTURES+= 	arch-lit.tex datarep-lit.tex
LECTURES+= 	shell-lit.tex
LECTURES+= 	python-lit.tex
LECTURES+= 	tex-lit.tex
LECTURES+= 	present-lit.tex

USE_LATEXMK= 	yes
USE_BIBLATEX= 	yes

studyguide.pdf studyguide.ps: ${FILES}

#export no

Makefile.export: Makefile
PACKAGE_FILES=	${FILES:.tex=.exporttex} Makefile.export

literature.bib: ../literature.bib
	${CP} $^ $@

install-aim.tex: ../labs/install/aims.tex
linux-aim.tex: ../labs/linux/aims.tex
pylab-aim.tex: ../labs/python/aims.tex
latex-aim.tex: ../labs/latex/aims.tex
sftp-aim.tex: ../labs/sftp/aims.tex
project-aim.tex: ../project/aims.tex

install-lit.tex: ../labs/install/literature.tex
linux-lit.tex: ../labs/linux/literature.tex
pylab-lit.tex: ../labs/python/literature.tex
latex-lit.tex: ../labs/latex/literature.tex
sftp-lit.tex: ../labs/sftp/literature.tex

intro-lit.tex: ../lectures/intro/literature.tex
datarep-lit.tex: ../lectures/datarep/literature.tex
arch-lit.tex: ../lectures/arch/literature.tex
shell-lit.tex: ../lectures/shell/literature.tex
python-lit.tex: ../lectures/python/literature.tex
tex-lit.tex: ../lectures/latex/literature.tex
present-lit.tex: ../lectures/present/literature.tex

${LABS} ${PM} ${SEMINARS} ${PROJECT} ${LECTURES}:
	${CP} $^ $@

clean:
	${RM} literature.bib ${LABS} ${PM} ${SEMINARS} ${PROJECT} ${LECTURES}

#endexport

### INCLUDES ###

miun.depend.mk:
ifeq (${MAKE},gmake)
	lynx -dump http://ver.miun.se/build/$@ > $@
else
	wget http://ver.miun.se/build/$@
endif

include miun.depend.mk
include miun.course.mk
include miun.package.mk
