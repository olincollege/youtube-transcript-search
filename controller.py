from model import YTSearchModel
from view import ViewTerminal

class Controller():

    def __init__(self):
        """
        !Docstring
        """
        self.view = ViewTerminal()
        self.model = YTSearchModel(self.view.channel, \
            self.split_keywords(self.view.keywords))

    def split_keywords(self, keywords):
        """
        Format raw user input data

        Args:
            keywords: a string of raw user input representing keywords

        Returns:
            A list of keywords to search for.
        """
        return keywords.split(", ")

    #* we can have methods here that interface between model and view