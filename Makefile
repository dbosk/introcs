SUBDIR= 	studyguide
SUBDIR+= 	labs
SUBDIR+= 	project
#SUBDIR+= 	lectures
#SUBDIR+= 	compendii

CATEGORY=	itgrund
PUB_FILES=	literature.bib

miun.depend.mk:
ifeq (${MAKE},gmake)
	lynx -dump http://ver.miun.se/build/$@ > $@
else
	wget http://ver.miun.se/build/$@
endif

include miun.depend.mk
include miun.subdir.mk
include miun.course.mk
