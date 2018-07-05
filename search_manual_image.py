from models import SearchConfig

class ManualSearchImage(SearchConfig):
    
    def __init__(self, config):
        self.config = config

    def search(self): 
        pass