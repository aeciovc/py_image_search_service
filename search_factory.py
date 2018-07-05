
from search_soup_html_image import HTMLSearchImage
from search_soup_lxml_image import LXMLSearchImage
from search_manual_image import ManualSearchImage

class SearchFactory(object):
    # Create based on class name:
    def factory(type, config):
        #return eval(type + "()")
        #if type == "ManualSearchImage": return ManualSearchImage(config)
        if type == "LXMLSearchImage": return LXMLSearchImage(config)
        if type == "HTMLSearchImage": return HTMLSearchImage(config)
        assert 0, "Bad search_image creation: " + type
    factory = staticmethod(factory)