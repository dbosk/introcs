CATEGORY=	itgrund/project
FILES=		project.tex literature.bib literature.tex
FILES+= 	report.pdf
DOCUMENTS=	project.pdf

USE_LATEXMK= 	yes
USE_BIBLATEX= 	yes

project.pdf: ${FILES}

#export no
TARBALL_FILES= 	${FILES} Makefile.export

report/report.pdf: report
	${MAKE} -C report report.pdf

report.pdf: report/report.pdf
literature.bib: ../literature.bib

report.pdf literature.bib:
	${CP} $^ $@

clean:
	${RM} literature.bib report.pdf
	${MAKE} -C report clean
#endexport

miun.depend.mk:
	wget http://ver.miun.se/build/$@

include miun.depend.mk
include miun.course.mk
