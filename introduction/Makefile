CATEGORY=	itgrund
FILES=		literature.tex ../itgrund.bib welcome.tex studyguide.tex \
			kursplan.pdf
DOCUMENTS=	literature.pdf welcome.pdf studyguide.pdf

literature.pdf: literature.tex ../itgrund.bib \
	../assignments/install/literature.tex \
	../assignments/terminal/literature.tex \
	../assignments/latex/literature.tex \
	../assignments/computer/literature.tex \
	../assignments/internet/literature.tex \
	../assignments/security/literature.tex \
	../assignments/sftp/literature.tex
welcome.pdf: welcome.tex kursplan.pdf
studyguide.pdf: studyguide.tex ../itgrund.bib

include miun.course.mk
