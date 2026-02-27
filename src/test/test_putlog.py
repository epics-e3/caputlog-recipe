import re

import pytest
from p4p.client.thread import Context


@pytest.fixture
def ctx(ioc):
    c = Context("pva")
    yield c
    c.close()


class TestPutLog:
    def test_can_connect(self, log_server, ioc):
        ioc.exit()

        assert "connected to log server" in ioc.outs + ioc.errs

    def test_has_all_macros(self, log_server, ioc):
        ioc.exit()

        assert not re.search(r"macLib: macro \S+ is undefined", ioc.outs + ioc.errs)

    def test_caput_triggers_log_message(self, log_server, ioc):
        import epics

        epics.caput("TEST:ai", 1)

        assert log_server.has_received_messages()

    def test_pvaput_triggers_log_message(self, log_server, ctx):
        ctx.put("TEST:ai", 1)

        assert log_server.has_received_messages()

    def test_multiple_pvaputs_produce_multiple_messages(self, log_server, ctx):
        ctx.put("TEST:ai", 1)
        ctx.put("TEST:ai2", 1)

        assert log_server.has_received_messages(2)


class TestJsonMessage:
    def test_has_required_attributes(self, log_server, ctx):
        ctx.put("TEST:ai", 1)

        log_server.has_received_messages()
        message = log_server.messages[0]

        assert "pv" in message
        assert "new" in message
        assert "old" in message

        assert "date" in message
        assert "time" in message
        assert "user" in message
        assert "iocName" in message
        assert "host" in message

    def test_has_additional_attributes_for_burst(self, log_server, ctx):
        ctx.put("TEST:ai", 1)
        ctx.put("TEST:ai", 1)

        log_server.has_received_messages()
        message = log_server.messages[0]

        assert "burst" in message
        assert "min" in message
        assert "max" in message

    def test_has_additional_attributes_for_waveform(self, log_server, ctx):
        ctx.put("TEST:wf", [1, 2, 3, 4])

        log_server.has_received_messages()
        message = log_server.messages[0]

        assert "old-size" in message
        assert "new-size" in message

    def test_has_correct_iocname(self, log_server, ctx):
        ctx.put("TEST:ai", 1)

        log_server.has_received_messages()
        message = log_server.messages[0]

        assert message["iocName"] == "TEST:CAPUTLOG"
