"""_summary_
"""
import sys
from model import YTSearchModel
from view import ViewTerminal


class Controller():
    """_summary_
    """

    def __init__(self):
        """
        Instantiate view and model classes.
        """
        # create view and get user input
        self.view = ViewTerminal()
        channel, keywords = self.view.get_search_input()
        self.model = YTSearchModel(channel, keywords.split(", "))

        self.view.draw_results(self.model.results)
        self.run_new_search()

    def run_new_search(self):
        """_summary_
        """
        again = self.view.search_again()
        if again == "y":
            channel, keywords = self.view.get_search_input()
            self.model.update_search(channel, keywords.split(", "))

            self.view.draw_results(self.model.results)
            self.run_new_search()
        else:
            sys.exit()

    # * we can have methods here that interface between model and view
