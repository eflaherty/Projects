import pytest
from server import SimpleHandler
from server import SimpleServer

h = SimpleHandler()
s = simpleServer()

class TestServer(object):
    def test_response(self):
        s.run()
        h.do_GET()
        h.respond(self, 200, "Hello, world!")


    def test_close(self):
        c.close()
        assert None == c.connection

    def test_get(self):
        response = c.get('/hello')
	assert 200 == response 
