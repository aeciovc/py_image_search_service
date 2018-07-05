from search_factory import SearchFactory

class SearchImages():
    
    def get(self, search_config):
        
        if search_config:
            search_service = SearchFactory.factory("LXMLSearchImage", search_config)
            image_list = search_service.search()
            
            return image_list
        else:
            return []