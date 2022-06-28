## The following lines are mandatory, please don't change them.
where_am_I := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
include $(E3_REQUIRE_TOOLS)/driver.makefile



## Exclude linux-ppc64e6500
##EXCLUDE_ARCHS = linux-ppc64e6500


APP:=caPutLogApp
APPSRC:=$(APP)

HEADERS += $(APPSRC)/caPutLog.h
HEADERS += $(APPSRC)/caPutLogTask.h
HEADERS += $(APPSRC)/caPutLogAs.h

HEADERS += $(APPSRC)/caPutJsonLogTask.h

SOURCES += $(APPSRC)/caPutLogTask.c
SOURCES += $(APPSRC)/caPutLogAs.c
SOURCES += $(APPSRC)/caPutLogClient.c
SOURCES += $(APPSRC)/caPutLog.c
SOURCES += $(APPSRC)/caPutLogShellCommands.c

SOURCES += $(APPSRC)/caPutJsonLogTask.cpp
SOURCES += $(APPSRC)/caPutJsonLogShellCommands.cpp

DBDS += $(APPSRC)/caPutLog.dbd
DBDS += $(APPSRC)/caPutJsonLog.dbd

SCRIPTS += ./iocsh/caPutLog.iocsh


db: 

.PHONY: db 


vlibs:

.PHONY: vlibs
