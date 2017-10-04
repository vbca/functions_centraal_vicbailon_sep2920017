import urllib.request
import json
import urllib.parse
import my_exceptions
import sys, os
import logger

class WebService:
    url = ''
    __user_id=''
    __user_pass=''
    __user_name=''
    __log = logger.Log()
    __file = os.path.basename(__file__)
        
    def __init__(self,url=None):
        self.url=url

    def login(self,useremail,password): 
        mydata= {'username':useremail,'password':password}
        headers={'Content-Type':'application/json'}
        response=self.__sendRequest(headers,'/api/login_json.php',mydata)
        if(int(response['status'])==200):
            self._user_id=useremail
            self._user_pass=password
            self._user_name=response['name']
            return True
        else:
            False

    def getContacts(self): 
        mydata= {'username':self.user_id,'password':self.user_pass}
        headers={'Content-Type':'application/json'}
        response=self.__sendRequest(headers,'/api/select_json.php',mydata)
        if(int(response['status'])==200):
            return response['content']    
        else:
            False

    def __sendRequest(self,header,action,data):
        localdata=json.dumps(data).encode('utf8')
        req=self.__post_request(self.url+action,localdata,header)
        page = self.__request(req,action)
        response= self.__get_read_from_request(page)
        response= json.loads(response)
        return response
    
    def __request(self,req,action):
        try:
            response = urllib.request.urlopen(req)
            self.__log.info(self.__file, 'request', 'url request successfull')
            self.__log.debug(self.url+action)
            return response
        except Exception as err:
            raise my_exceptions.CustomError("Error en la url", sys.exc_info())

    def __post_request(self,url,data,header):
        try:
            return urllib.request.Request(url, data, header)
        except:
            raise my_exceptions.CustomError("No se puede leer el request", sys.exc_info())
            

    def __get_read_from_request(self, request):
        try:
            return request.read()
        except:
            raise my_exceptions.CustomError("No se puede leer el request", sys.exc_info())

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def user_pass(self):
        return self._user_pass

    @user_pass.setter
    def user_pass(self, value):
        self._user_pass= value