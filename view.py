"""
View classes for YouTube transcript search.
"""
from abc import ABC


class View(ABC):
    """
    Abstract base class for view.
    """

    def __init__(self):
        """
        Create initial interface.
        """

    def get_search_input(self, available_channels):
        """
        Get the channel and keywords from the user.
        """

    def draw_results(self, results):
        """
        Return the results of the search to the user

        Args:
            results: a list of YouTube videos in order of relevance.
        """


class ViewTerminal(View):
    """_summary_

    Attributes:
        repeat (_type_): _description_
    """

    def __init__(self):
        """
        Display interface
        """
        super().__init__()
        self.repeat = ""
        print("\n---YouTube transcript search---")
        print("\nSearch every video on a YouTube channel for a " +\
            "keyword or words.")

    def get_search_input(self, available_channels):
        """
        Get the channel and keywords from the user.

        Args:
            available_channels: list of channels that have already been
            downloaded locally by the user.
        """
        while True:
            print("\nThe channels that are currently available to search are:")
            for channel in available_channels:
                print(" | " + channel)

            channel = input("\nWhich channel would you like to search? ")

            # if the channel is not already downloaded locally, confirm that the
            # user would like to download it.
            if channel not in available_channels:
                new_channel = input("\nThis channel is not downloaded, and \
                    will take some time to download, would you like to \
                    continue? (y/n): ")
                if new_channel == "y":
                    break
            else:
                break
        print("\nYou are searching for videos on the YouTube channel " +\
                f"[{channel}]")

        keywords = input("\nEnter comma separated keywords/phrases: ")

        # indicate search is in progress
        print("\nSearching video transcripts...")

        return (channel, keywords)

    def draw_results(self, results):
        """
        Show user the results of the search (video title and URL).

        Args:
            results: a list of YouTube videos in order of relevance.
        """
        print("------------")
        for item in results:
            print(f"\n{item[0]} \n- Score: {item[1]}")

    def search_again(self):
        """
        Ask user if they want to make another search.

        Returns:
            user input (y/n) indicating if they want to search again
        """
        self.repeat = input("Do you want to search again? (y/n): ")
        return self.repeat
