from yt_search_model import YTSearchModel
from yt_search_view_terminal import YTSearchViewTerminal

class YTSearchController():

    def __init__(self):
        self.view = YTSearchViewTerminal()
        self.model = YTSearchModel()
    
    def channel_in_database(self):
        # Check if 
