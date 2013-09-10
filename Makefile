SUBDIR= 	studyguide
SUBDIR+= 	labs
SUBDIR+= 	project
SUBDIR+= 	lectures
#SUBDIR+= 	compendii

CATEGORY=	itgrund
PUB_FILES=	literature.bib

miun.depend.mk:
	wget http://ver.miun.se/build/$@

include miun.depend.mk
include miun.subdir.mk
include miun.course.mk
