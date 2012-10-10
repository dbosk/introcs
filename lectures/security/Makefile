CATEGORY=	itgrund/lectures
FILES=		security.tex ../../literature.bib
DOCUMENTS=	security.pdf

security.pdf: security.tex ../../literature.bib order.eps letter_of_rec.eps

order.eps: order.ps
	ps2eps order.ps
letter_of_rec.eps: letter_of_rec.ps
	ps2eps letter_of_rec.ps

clean: clean-course
	${RM} letter_of_rec.eps order.eps

include miun.course.mk
