from connectors.core.connector import Connector, get_logger, ConnectorError
from .constants import LOGGER_NAME
from .operations import check, operations

logger = get_logger(LOGGER_NAME)


class Chatsonic(Connector):

    def execute(self, config, operation, params, *args, **kwargs):
        try:
            action = operations.get(operation)
            return action(config, params)
        except Exception as err:
            raise ConnectorError("Message: {0}".format(err))

    def check_health(self, config=None, *args, **kwargs):
        return check(config)
