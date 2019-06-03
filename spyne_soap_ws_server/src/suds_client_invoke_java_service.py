'''
Created on Aug 23, 2017

@author: SummitWorks
'''
from suds.client import Client
hello_client = Client('http://localhost:3333/ws/person?wsdl')
#print(hello_client.service.say_hello("Dave", 5))
print(hello_client)
print(hello_client.service.Fibonacci(10))
# JavaWebservicesJAX-WS-DocumentStyle-Server in spring 2017 work space 
# hello_client = Client('http://localhost:7779/ws/hello?wsdl')
# print(hello_client)
# print(hello_client.service.getHelloWorldAsString("Maruthi Python SOAP"))