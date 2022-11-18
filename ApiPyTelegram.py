class ApiPyTelegramExceptor(Exception):
    pass
import requests
import logging
import sys
global ver
ver = 0.1
logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
    datefmt="%d/%b/%Y %H:%M:%S",
    stream=sys.stdout)
log = logging.getLogger("apt")
class apt():
    def __init__(self, in_token) -> None:
        global out_token
        out_token = in_token
        log.debug("Setted '{0}' secret token with '{1}' in-program token".format(out_token,in_token))
    def version():
        return ver
    def DebugMessageEnabled(bool=None):
        if bool == True:
            return 
        elif bool == False:
            logging.shutdown()
        elif bool == None:
            return bool
class message():
    def text(chat_id,text):
        response = requests.post('https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}'.format(out_token, chat_id, text.replace(" ", "+"))) 
        try:
            log.critical("Telegram api error: {0}".format(response.json()["description"]))
            raise ApiPyTelegramExceptor("Telegram api error: {0}".format(response.json()["description"]))
        except KeyError:
            log.info("Sended '{0}' with http code '{1}'".format(text, response.status_code))
        return response.status_code




