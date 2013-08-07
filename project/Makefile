CATEGORY=	itgrund/project
FILES=		project.tex literature.bib literature.tex
DOCUMENTS=	project.pdf

USE_LATEXMK= 	yes
USE_BIBLATEX= 	yes

project.pdf project.ps: ${FILES}

#export no
TARBALL_FILES= 	${FILES} Makefile.export

literature.bib: ../literature.bib
	${CP} $^ $@

clean:
	${RM} literature.bib
#endexport

miun.depend.mk:
ifeq (${MAKE},gmake)
	lynx -dump http://ver.miun.se/build/$@ > $@
else
	wget http://ver.miun.se/build/$@
endif

include miun.depend.mk
include miun.course.mk
