from decouple import config

import logging

#Logger
logger = logging.getLogger(config('SERVICE_NAME'))

#Formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

#Handler
handler = logging.FileHandler(config('SERVICE_NAME')+'.log')
handler.setFormatter(formatter)

logger.addHandler(handler)

def info(msg):
    logger.info(msg)