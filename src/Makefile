## The following lines are mandatory, please don't change them.
include $(E3_REQUIRE_TOOLS)/driver.makefile

USR_CPPFLAGS += -DJSON_AND_ARRAYS_SUPPORTED

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

DBDS += $(APPSRC)/caPutJsonLog.dbd

SCRIPTS += ./iocsh/caPutLog.iocsh
