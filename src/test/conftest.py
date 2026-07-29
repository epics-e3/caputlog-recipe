import socketserver
import json
import threading
import time
import logging
from pathlib import Path

import pytest
from run_iocsh import IOC

LOG = logging.getLogger(__name__)

DATA_DIR = Path(__file__).parent

LOG_SERVER_IP = "127.0.0.1"
LOG_SERVER_PORT = 8002

TIMEOUT = 10.0  # caPutLog is slow to send buffered messages


class JsonLogHandler(socketserver.StreamRequestHandler):
    def handle(self):
        for line in self.rfile:
            line = line.strip()
            if not line:
                continue
            self.server.messages.append(json.loads(line))


class LogServer(socketserver.TCPServer):
    def __init__(self, host=LOG_SERVER_IP, port=LOG_SERVER_PORT):
        super().__init__((host, port), JsonLogHandler)
        self.messages = []

    def has_received_messages(self, count=1, timeout=TIMEOUT):
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            if len(self.messages) >= count:
                return True
            time.sleep(0.05)
        LOG.error("No log messages received in time")
        return False


@pytest.fixture
def ioc():
    with IOC.ready(
        (DATA_DIR / "ioc" / "st.cmd").as_posix(),
        "--iocname",
        "TEST:CAPUTLOG",
    ) as ioc_proc:
        yield ioc_proc
    # Dump logs on test failure
    LOG.error("IOC stdout:\n%s", ioc_proc.stdout)
    LOG.error("IOC stderr:\n%s", ioc_proc.stderr)


@pytest.fixture(scope="session")
def log_server():
    server = LogServer()
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield server
    server.shutdown()


@pytest.fixture(autouse=True)
def clear_log_messages(log_server):
    log_server.messages.clear()
