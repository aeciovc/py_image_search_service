from bs4 import BeautifulSoup
from logging import info

import urllib.request
import json
import time

#Modules
from models import SearchConfig, Image

class HTMLSearchImage(SearchConfig):
    
    def __init__(self, config):
        self.config = config

    def search(self): 
        info("[LXMLSearchImage] searching for " + self.config.query)

        start_time = time.time()
        url=self.config.get_search_url()
        info("[LXMLSearchImage] Requesting... "+ url)
        
        #Headers
        header={'User-Agent':self.config.user_agent}
        
        #Request
        soup = get_soup(url,header)

        image_list=[]
        for a in soup.find_all("div",{"class":"rg_meta"}):
            #link,Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"] #Original Image
            link,Type =json.loads(a.text)["tu"],json.loads(a.text)["ity"]
            
            #Create Image object and put on list
            image = Image(link, Type)
            image_list.append(image)

        info("[LXMLSearchImage] there are total "+ str(len(image_list)) +" images")
        elapsed_time = time.time() - start_time
        info("[LXMLSearchImage] Total time elapsed: " + str(elapsed_time))
        return image_list

def get_soup(url,header):
    return BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url,headers=header)),'html.parser')