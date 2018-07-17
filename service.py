from nameko.rpc import rpc
from nameko.web.handlers import http
from decouple import config

#Models and Controllers
from models import SearchConfig
from controller import SearchImagesController

import json

#Intern Modules
from logger import default

class ImageService:
    name = config('SERVICE_NAME')

    #Configs
    MAX_IMAGES = config('MAX_IMAGES_RETURN')
    SEARCH_URL = config('SEARCH_URL')
    USER_AGENT = config('USER_AGENT')

    #RPC methods
    @rpc
    def ping(self):
        return "pong!"

    @rpc
    def search(self, query):

        #Config Search
        search_config = SearchConfig(query, self.MAX_IMAGES, self.SEARCH_URL, self.USER_AGENT)

        image_list = SearchImagesController().get(search_config)
        results = json.dumps([ob.as_json() for ob in image_list])
        return results

    #HTTP methods
    '''
    @http('GET', '/ping')
    def ping(self, request):
        return "pong"

    @http('GET', '/search/<string:query>')
    def search(self, request, query):
        image_list = SearchImages().get(search_config)
        results = json.dumps([ob.as_json() for ob in image_list])
        return results
    '''