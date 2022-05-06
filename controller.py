"""
Controller for YouTube transcript search.
"""
import sys
import os
from model import YTSearchModel
from view import ViewTerminal, error

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

        self.model = None

        def run_init_search(channel, keywords):
            """
            Run initial search where model class is instantiated.
            Recursive for error handeling.

            Args:
                channel: a string of raw user input representing channel
                keywords: a string of raw user input representing keywords
            """
            try:
                self.model = YTSearchModel(channel, keywords.split(", "),\
                    self.available_channels)
                # if it works, return the successful title and keywords
            except FileNotFoundError:
                # alert user to error
                error(1)
                # ask for new input
                channel_new, keywords_new = self.view.get_search_input(self.\
                    available_channels)
                # try again
                run_init_search(channel_new, keywords_new)

        # run search
        run_init_search(channel,keywords)

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

            # define recursive search function
            def update_model(channel, keywords):
                """
                Recursive error handeling

                Args:
                channel: a string of raw user input representing channel
                keywords: a string of raw user input representing keywords
                """
                try:
                    # update model and run search
                    self.model.update_search(channel, keywords.split(", "),\
                        self.available_channels)

                except FileNotFoundError:
                    # alert user to error
                    error(1)
                    # ask for new input
                    channel_new, keywords_new = \
                    self.view.get_search_input(self.available_channels)
                    # recursively run search again
                    update_model(channel_new, keywords_new)

            # run search
            update_model(channel, keywords)

            # display results
            self.view.draw_results(self.model.results)
            # ask if user wants to search again
            self.run_new_search()
        else:
            sys.exit()

    def update_available_channels(self):
        """
        Update the record of channels stored locally by the user.
        """
        # list of channels already downloaded
        if len(os.listdir('./transcript_data')) != 0:
            self.available_channels = next(os.walk('./transcript_data'))[1]
