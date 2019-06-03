'''
Created on Aug 23, 2017

@author: SummitWorks
'''
from spyne.application import Application
from spyne.decorator import srpc
from spyne.service import ServiceBase
from spyne.model.complex import Iterable
from spyne.model.primitive import UnsignedInteger
from spyne.model.primitive import String
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
from spyne.protocol.soap import Soap11

class FibonanciService(ServiceBase):
    
    @srpc(UnsignedInteger, _returns=Iterable(UnsignedInteger))
    def Fibonacci(n):

        a, b = 0, 1
        while True:
            if a > n: return
            yield a
            a, b = b, a+b



if __name__=='__main__':
    import logging

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)
    app = Application([FibonanciService], 'spyne.examples.hello.http',
        in_protocol=Soap11(validator='lxml'),
        out_protocol=Soap11(),
    )
    wsgi_app = WsgiApplication(app)
    server = make_server('127.0.0.1', 3333, wsgi_app)

    print("listening to http://127.0.0.1:3333")
    print("wsdl is at: http://localhost:3333/?wsdl")

    server.serve_forever()