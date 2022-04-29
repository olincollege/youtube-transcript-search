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
        print("\n---YouTube transcript search---")
        print("\nSearch every video on a YouTube channel for a keyword or words.")

    def get_search_input(self, available_channels):
        """
        Get the channel and keywords from the user.
        """

        while True:
            print("\nThe channels that we have stored are:")
            for channel in available_channels:
                print("- " + channel)

            channel = input("\nWhich channel would you like to search? ")

            if channel not in available_channels:
                new_channel = input("\nThis channel is not downloaded, and will \
                    take some time to download, would you like to continue? \
                    (y/n) ")
                if new_channel == "y":
                    break
            else:
                break
        print(
            f"\nYou are searching for videos on the YouTube channel [{channel}]")

        keywords = input("\nEnter comma separated keywords/phrases: ")

        print("\nSearching video transcripts...")

        return (channel, keywords)

    def draw_results(self, results):
        # Display URL/title results of search

        # print URL and title

        print("------------")
        for item in results:
            print(f"\n{item[0]} \n- Score: {item[1]}")

    def search_again(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        self.repeat = input("Do you want to search again? (y/n): ")
        return self.repeat
