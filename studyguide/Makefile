# $Id$

DOCUMENTS=	studyguide.pdf
CATEGORY=	itgrund
FILES=		studyguide.tex literature.bib \
			${LABS} ${SEMINARS} ${PM} ${PROJECT} ${LECTURES}
PACKAGE=	studyguide-src
PACKAGE_FILES=	${FILES} Makefile
PUB_FILES=	${DOCUMENTS} ${PACKAGE}.tar.gz

LABS=		inst-aim.tex inst-lit.tex
LABS+= 		term-aim.tex term-lit.tex
LABS+= 		pylab-aim.tex pylab-lit.tex
LABS+= 		computer-aim.tex computer-lit.tex
#LABS+= 		sftp-aim.tex sftp-lit.tex
SEMINARS=
PM=
PROJECT=	project-aim.tex
LECTURES=	intro-lit.tex
LECTURES+= 	arch-lit.tex datarep-lit.tex
LECTURES+= 	shell-lit.tex
LECTURES+= 	python-lit.tex
LECTURES+= 	tex-lit.tex
LECTURES+= 	report-lit.tex

USE_LATEXMK= 	yes
USE_BIBLATEX= 	yes

studyguide.pdf studyguide.ps: ${FILES}

#export no

Makefile.export: Makefile
PACKAGE_FILES=	${FILES:.tex=.exporttex} Makefile.export

literature.bib: ../literature.bib
	${CP} $^ $@

inst-aim.tex: ../labs/install/aims.tex
term-aim.tex: ../labs/terminal/aims.tex
pylab-aim.tex: ../labs/python/aims.tex
latex-aim.tex: ../labs/latex/aims.tex
computer-aim.tex: ../labs/computer/aims.tex
sftp-aim.tex: ../labs/sftp/aims.tex
project-aim.tex: ../project/aims.tex

inst-lit.tex: ../labs/install/literature.tex
term-lit.tex: ../labs/terminal/literature.tex
pylab-lit.tex: ../labs/python/literature.tex
latex-lit.tex: ../labs/latex/literature.tex
computer-lit.tex: ../labs/computer/literature.tex
sftp-lit.tex: ../labs/sftp/literature.tex

intro-lit.tex: ../lectures/intro/literature.tex
datarep-lit.tex: ../lectures/datarep/literature.tex
arch-lit.tex: ../lectures/arch/literature.tex
shell-lit.tex: ../lectures/shell/literature.tex
python-lit.tex: ../lectures/python/literature.tex
tex-lit.tex: ../lectures/latex/literature.tex
report-lit.tex: ../lectures/report/literature.tex

${LABS} ${PM} ${SEMINARS} ${PROJECT} ${LECTURES}:
	${CP} $^ $@

clean:
	${RM} literature.bib ${LABS} ${PM} ${SEMINARS} ${PROJECT} ${LECTURES}

#endexport

### INCLUDES ###

miun.depend.mk:
	wget http://ver.miun.se/build/$@

include miun.depend.mk
include miun.course.mk
include miun.package.mk
