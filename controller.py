"""_summary_
"""
import sys
import os
from model import YTSearchModel
from view import ViewTerminal


class Controller():
    """_summary_
    """

    def __init__(self):
        """
        Instantiate view and model classes.
        """

        # Find all channels that have been downloaded from Youtube
        self.available_channels = next(os.walk('./transcript_data'))[1]

        # create view and get user input
        self.view = ViewTerminal()
        channel, keywords = self.view.get_search_input(self.available_channels)
        self.model = YTSearchModel(channel, keywords.split(", "),
                                   self.available_channels)

        self.view.draw_results(self.model.results)
        self.run_new_search()

    def run_new_search(self):
        """_summary_
        """
        again = self.view.search_again()
        if again == "y":
            self.available_channels = next(os.walk('./transcript_data'))[1]

            channel, keywords = \
                self.view.get_search_input(self.available_channels)
            self.model.update_search(channel, keywords.split(", "),
                                     self.available_channels)

            self.view.draw_results(self.model.results)
            self.run_new_search()
        else:
            sys.exit()

    # * we can have methods here that interface between model and view
