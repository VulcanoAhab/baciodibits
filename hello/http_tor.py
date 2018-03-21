import re
import json
import socks
import socket
from http.client import HTTPResponse

class Blink:
    """ 
    """ 
    _tor_port=9050
    _rexip=re.compile(r"(\d{1,3}\.){4}")
    _GET="GET {url} HTTP/1.1\r\n"\
         "Host: {host}\r\n"\
         "User-Agent: Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko\r\n\r\n"
    

    @classmethod
    def set_tor_port(cls, port):
        """
        """
        cls._tor_port=port
    
    @classmethod
    def _isip(cls, value):
        """
        """
        _ispi=cls._rexip.search(value)
        if not _ispi:return False
        return True

    def __init__(self, host, port=80):
        """
        """
        self._host=host
        self._port=port
        self._ipv4=None
        self._addrinfo=tuple()
        self._socket=socket
        self._socks=socks
        self._socks.set_default_proxy(socks.SOCKS5, 
                                      "127.0.0.1",
                                      self._tor_port)    
        self._socket.socket=self._socks.socksocket

    def ipv4ByName(self):
        """
        """
        if self._addrinfo:return self._addrinfo
        self._ipv4=self._host
        if not self._isip(self._host):
            self._ipv4=self._socket.gethostbyname(self._host)
        self._addrinfo=(self._ipv4, self._port)
        return self._addrinfo
    
    def connect(self):
        """
        """
        pass
    
    def send_request(self):
        """
        """
        pass
    
    def read_response(self):
        """
        """
        pass
    
    def myIp(self):
        """
        """
        #translate if domain
        self.ipv4ByName()
        #request
        hostName="www.httpbin.org"
        request=self._GET.format(url="/ip", host=hostName)
        ipv4=self._socket.gethostbyname(hostName)
        #test ip
        sockis=self._socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        sockis.connect((ipv4,80))
        sockis.sendall(request.encode())
        res=HTTPResponse(sockis)
        res.begin()
        msg=res.read(1024)
        response={
            "status":res.status,
            "ip":json.loads(msg.decode())["origin"]
            "rawResponse":msg
            }
        sockis.close()
        return response
    

