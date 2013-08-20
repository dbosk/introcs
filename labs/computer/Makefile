CATEGORY=	itgrund/assignments
FILES=		computer.tex literature.tex aims.tex literature.bib
DOCUMENTS=	computer.pdf

USE_LATEXMK= 	yes
USE_BIBLATEX= 	yes

computer.pdf computer.ps: computer.tex literature.bib

#export no
literature.bib: ../../literature.bib
	${CP} $^ $@

TARBALL_FILES= 	${FILES:.tex=.exporttex} Makefile.export

clean:
	${RM} computer.pdf computer.ps literature.bib
#endexport

miun.depend.mk:
ifeq (${MAKE},gmake)
	lynx -dump http://ver.miun.se/build/$@ > $@
else
	wget http://ver.miun.se/build/$@
endif

include miun.depend.mk
include miun.course.mk
