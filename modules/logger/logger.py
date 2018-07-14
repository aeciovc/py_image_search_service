'''Logger: Log activities with support for monitoring tools'''

import logging
import json

# setup logging
with open("modules/logger/logging.json", "r", encoding="utf-8") as fd:
    logging.config.dictConfig(json.load(fd))

#Root log
logger = logging.getLogger()
logger.name = "root.service"

#New Relic Logger
logger_new_relic = logging.getLogger("newrelic")

class NewRelicLogger(object):

    def __init__(self, config):
        self.config = config #TODO It should get new relic config

    def info(self, msg):
        logger_new_relic.info(msg)

    def error(self, msg):
        logger.error(msg)
        logger_new_relic.error(msg) #TODO It should send error log for new relic app

    def critical(self, msg):
        logger.critical(msg)
        logger_new_relic.critical(msg) #TODO It should send critical log for new relic app