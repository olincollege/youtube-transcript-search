
from model import YTSearchModel
from view import ViewTerminal


class Controller():

    def __init__(self):
        """
        Instantiate view and model classes.
        """
        # create view and get user input
        self.view = ViewTerminal()
        channel, keywords = self.view.get_search_input()
        self.model = YTSearchModel(channel, self.split_keywords(keywords))

        self.view.draw_results(self.model.results)
        self.run_new_search()

    def split_keywords(self, keywords):
        """
        Format raw user input data

        Args:
            keywords: a string of raw user input representing keywords

        Returns:
            A list of keywords to search for.
        """
        return keywords.split(", ")

    def run_new_search(self):
        """_summary_
        """
        again = self.view.search_again()
        if again == "y":
            channel, keywords = self.view.get_search_input()
            self.model.update_search(channel, self.split_keywords(keywords))

            self.view.draw_results(self.model.results)
            self.run_new_search()
        else:
            quit()

    # * we can have methods here that interface between model and view
