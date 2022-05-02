"""
Controller for YouTube transcript search.
"""
import sys
import os
from model import YTSearchModel
from view import ViewTerminal


class Controller():
    """
    Control and interface between view and model classes.
    """

    def __init__(self):
        """
        Instantiate the View and Model classes and run the initial search with
        user input.
        """
        # find channels that are already downloaded
        self.available_channels = []
        self.update_available_channels()

        # instantiate view
        self.view = ViewTerminal()

        # get user input for search
        channel, keywords = self.view.get_search_input(self.available_channels)

        # run search
        self.model = YTSearchModel(channel, keywords.split(", "), self.available_channels)

        # display results to user
        self.view.draw_results(self.model.results)

        # ask the user if they want to run another search
        self.run_new_search()

    def run_new_search(self):
        """
        Run additional searches after the initial search.
        """
        # ask user if they want to search again
        again = self.view.search_again()
        # if user wants to search again run the whole process over again
        if again == "y":
            # Update list of available channels
            self.update_available_channels()
            
            # get user input
            channel, keywords = \
                self.view.get_search_input(self.available_channels)
            # update model and run search
            self.model.update_search(channel, keywords.split(", "), self.available_channels)

            # display results
            self.view.draw_results(self.model.results)
            # ask if user wants to search again
            self.run_new_search()
        else:
            sys.exit()

    def update_available_channels(self):
        """
        Update record of channels stored locally by the user.
        """
        # list of channels already downloaded
        if len(os.listdir('./transcript_data')) != 0:
            self.available_channels = next(os.walk('./transcript_data'))[1]

