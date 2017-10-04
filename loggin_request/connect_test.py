from webfunctions import WebService
site = WebService('http://localhost:8888/agenda')
site.login('victorg@mx1.ibm.com','12345bailon')
a=site.getContacts()
print(a)