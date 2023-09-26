import requests
import logging
import re
from bs4 import BeautifulSoup
from requests_toolbelt.utils import dump
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME

logger = get_logger(LOGGER_NAME)
#logger.setLevel(logging.DEBUG) # Uncomment to enable local debug


class ChatSonic:
    supported_languages = ["en","nl","fr","de","it","pl","es","ru","ja","zh","bg","cs","da","el","hu","lt","lv","ro","sk","sl","sv","fi","et"]
    def __init__(
            self,
            *,
            api_key,
            engine: str = "premium",
            timeout: int = 60,
            logger=None
    ) -> None:
        self.base_url = "https://api.writesonic.com"
        self.api_key = api_key
        self.engine = engine
        self.timeout = timeout
        self.logger = logger

    def send_message(
            self,
            *,
            language: str = "en",
            google_enabled: bool = False,
            history_data: list = [],
            input_text: str,
    ) -> dict:
        language = language if language in ChatSonic.supported_languages else "en"
        enable_memory = True if len(history_data) > 0 else False
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-API-KEY": self.api_key,
        }

        req_payload = {
            "input_text": input_text,
            "history_data": history_data,
            "enable_google_results": google_enabled,
            "enable_memory": enable_memory
        }

        params = {
            "engine": self.engine,
            "language": language
        }
        try:
            response = requests.post(
                url=f"{self.base_url}/v2/business/content/chatsonic",
                headers=headers,
                json=req_payload,
                params=params,
                timeout=self.timeout
            )
            self.logger.debug('\nRequest: \n{}\n'.format(dump.dump_all(response).decode('utf-8')))
            if response.ok:
                return response.json()
            else:
                logger.exception("Request failed:{}".format(response.text))
                raise

        except Exception as err:
            logger.exception(err)
            raise ConnectorError(err)

def remove_tags(text):
    tag_stripped = BeautifulSoup(text, "html.parser").text
    return re.sub(r'#\w+(\s+)?','',tag_stripped)

def prep_action_parameters(params):
    '''
    parse params
    '''
    try:
        paramters = {key.split('@')[1].lower(): value for key, value in params.items() if "param@" in key}
        paramters.update({'input_text': remove_tags(paramters['input_text'])})
        if 'history_data' in paramters and len(paramters['history_data']) > 0:
            for msg in paramters['history_data']:
                if msg['is_sent']:
                    msg.update({'message':remove_tags(msg['message'])})
        return paramters
    except Exception as Err:
        logger.error('Could not parse params [{0}] '.format(Err))
        raise ConnectorError(Err)

def chat_completions(config, params):
    chatsonic = ChatSonic(api_key=config.get('api_key'), logger=logger)
    parameters = prep_action_parameters(params)
    return chatsonic.send_message(**parameters)


def check(config):
    try:
        chat_completions(config, {"param@input_text": "what time is it"})
    except Exception as err:
        logger.error('{0}'.format(err))
        raise ConnectorError('{0}'.format(err))


operations = {
    'chat_completions': chat_completions,
    'chat_conversation': chat_completions
}