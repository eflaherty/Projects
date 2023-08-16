import pytest
from client import SimpleHTTPClient

c = SimpleHTTPClient('127.0.0.1', 8080)

class TestClient(object):
    def test_connect(self):
        c.connect()
        assert '127.0.0.1' == c.serverHost
        assert 8080 == c.serverPort

    def test_close(self):
        c.close()
        assert None == c.connection

    def test_get(self):
        response = c.get('/hello')
	assert 200 == response 
