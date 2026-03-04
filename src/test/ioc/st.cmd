require caputlog

asSetFilename("$(E3_CMD_TOP)/test.acf")
iocshLoad("$(caputlog_DIR)/caPutLog.iocsh", "CAPUTLOG_INET=127.0.0.1")

dbLoadRecords("$(E3_CMD_TOP)/test.db")
