from model import YTSearchModel
from view import ViewTerminal

class YTSearchController():

    def __init__(self):
        self.view = ViewTerminal()
        self.model = YTSearchModel(self.view.chosen_channel, \
            self.split_keywords(self.view.keywords))

    def split_keywords(self, keywords):
        return keywords.split(", ")
    
    def channel_in_database(self):
        # Check if 
        pass
