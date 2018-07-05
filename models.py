from urllib import parse

class SearchConfig(object):
    
    def __init__(self, query, max_results, search_url, user_agent):
        self.query = parse.quote(query)
        self.max_results = max_results
        self.search_url = search_url
        self.user_agent = user_agent

    def get_search_url(self):
        query = self.query
        query= query.split()
        query='+'.join(query)

        return self.search_url.replace('<query>', query)
    
class Image(object):

    def __init__(self, address, content_type):
        self.address = address
        self.content_type = content_type

    def as_json(self):
        return dict(
            address=self.address, 
            content_type=self.content_type)

    def __str__(self):
        return self.address