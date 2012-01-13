include inc.mk
include pub.mk

TEXDIRS?=inl-1.3 inl-2.5 inl-2.6 inl-3.1 inl-3.2 inl-3.3
LABDIRS?=
SUBDIRS?=${TEXDIRS} ${LABDIRS}


.PHONY: all clean struct publish-all index packages


all:
	-for dir in ${SUBDIRS}; do \
		cd $${dir} && ${MAKE} all; cd ..; \
		done
clean:
	-for dir in ${SUBDIRS}; do \
		cd $${dir} && ${MAKE} clean; cd ..; \
		done

struct:
	-for dir in ${TEXDIRS}; do \
		${MKDIR} -p $${dir}; \
		${CP} templates/Makefile $${dir}/Makefile; \
		${CP} *.mk $${dir}; \
		${CP} templates/{aim,instructions,grading,exercises,handin}.tex \
			$${dir}; \
		${CP} templates/inl-X_Y.tex $${dir}/$${dir}.tex; \
		cd $${dir} && ${MAKE} struct; cd ..; \
		done
	-for dir in ${LABDIRS}; do \
		${MKDIR} -p $${dir}; \
		${CP} ../templates/Makefile.lab $${dir}/Makefile; \
		${CP} ../templates/Makefile.code $${dir}; \
		${CP} *.mk $${dir}; \
		cd $${dir} && ${MAKE} struct; cd ..; \
		done

index:
	${EDITOR} index.html && ${CP} index.html index.css ${PUBDIR}/

publish-all: index
	-for dir in ${SUBDIRS}; do \
		cd $${dir} && ${MAKE} publish; \
		done

packages:
	@for dir in ${SUBDIRS}; do \
		${TAR} -zcf $${dir}.tgz $${dir}; \
		done

print-all:
	@for dir in ${SUBDIRS}; do \
		cd $${dir} && ${MAKE} print; \
		cd ..; \
		done
