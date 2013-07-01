CATEGORY=	itgrund
FILES=		welcome.tex kursplan.pdf studyguide.pdf
DOCUMENTS=	welcome.pdf

PACKAGE=		intro-src
PACKAGE_FILES=	${FILES} Makefile

PUB_FILES=		${PACKAGE}.tar.gz ${DOCUMENTS}

welcome.pdf welcome.ps: ${FILES}

#export no

PACKAGE_FILES=	${FILES:.tex=.exporttex} Makefile.export

studyguide.pdf: ../studyguide/studyguide.pdf
	${CP} $^ $@

../studyguide/studyguide.pdf:
	${MAKE} -C ../studyguide studyguide.pdf

#endexport

miun.depend.mk:
ifeq (${MAKE},gmake)
	lynx -dump http://ver.miun.se/build/$@ > $@
else
	wget http://ver.miun.se/build/$@
endif

include miun.depend.mk
include miun.course.mk
include miun.package.mk
