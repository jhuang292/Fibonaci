'''
Created on Aug 23, 2017

@author: SummitWorks
'''
from suds.client import Client
hello_client = Client('http://localhost:3333/?wsdl')
print(hello_client.service.say_hello("Maruthi", 5))