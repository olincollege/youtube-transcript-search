"""_summary_
"""
from abc import ABC


class View(ABC):
    """_summary_

    Args:
        ABC (_type_): _description_
    """
    def __init__(self):
        """_summary_
        """
        self.draw_interface()

    def draw_interface(self):
        """
        Display interface and prompt for user input
        """

    def get_search_input(self):
        """
        Get the channel and keywords from the user.
        """

    def draw_results(self, results):
        """
        Return the results of the search to the user

        Args:
            !results:
        """


class ViewTerminal(View):
    """_summary_

    Args:
        View (_type_): _description_
    """
    def __init__(self):
        """
        Display interface
        """
        self.repeat = ""
        self.draw_interface()
        print("---YouTube transcript search---")
        print("Search every video on a YouTube channel for a keyword or words.")

    def get_search_input(self):
        """
        Get the channel and keywords from the user.
        """
        channel = 'CrashCourse'  # ! default for now

        print(
            f"You are searching for videos on the YouTube channel {channel}")

        keywords = input("Enter comma separated keywords/phrases: ")

        print("Searching video transcripts...")

        return (channel, keywords)

    def draw_results(self, results):
        # Display URL/title results of search

        # print URL and title

        print("------------")
        print(results)

    def search_again(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        self.repeat = input("Do you want to search again? (y/n): ")
        return self.repeat
