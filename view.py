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
    """
    View class for terminal.

    Attributes:
        !repeat (_type_): _description_
    """

    def __init__(self):
        """
        Display interface
        """
        super().__init__()
        self.repeat = ""
        print("\n---YouTube transcript search---")
        print("Search every video on a YouTube channel"
            " for a keyword or words.")

    def get_search_input(self, available_channels):
        """
        Get the channel and keywords from the user.

        Args:
            available_channels: list of channels that have already been
            downloaded locally by the user.
        """
        # set default search message
        search_message = "Searching video transcripts..."
        while True:
            # if there are no available channels, prompt user to download one
            if len(available_channels) == 0:
                channel = input("\nYou don't have any channel data locally"
                            " downloaded. Enter the exact name of the YouTube"
                            " channel you would like to search: ")
                # update search message to reflect increased loading time
                search_message = ("Downloading transcript data and searching"
                " video transcripts. This may take a few minutes...")
                break

            # if there are already local channels
            else:
                print("\nThe channels that are currently available to search are:")
                for channel in available_channels:
                    print(" | " + channel)

                channel = input("\nWhich channel would you like to search? ")\
                    .strip() # remove unwanted spaces

                # if the channel is not already downloaded locally, confirm that
                # the user would like to download it.
                if channel not in available_channels:
                    new_channel = input("\nThis channel will need to be " "locally downloaded and the search will take longer than " "usual, would you like to continue? (y/n): ")
                    if new_channel == "y":
                    # update search message to reflect increased loading time
                        search_message = ("Downloading transcript data and"
                        " searching video transcripts. This may take a few"
                        " minutes...")
                        break
                else:
                    break # end the program

        keywords = ""
        while keywords == "":
            # get raw user search term input
            keywords = input("\nEnter comma separated keywords/phrases to"
                        f" search for on the YouTube channel {channel}: ")

        # indicate search (and possibly download) is in progress
        print("\n" + search_message)
        return (channel, keywords.strip())

    def draw_results(self, results):
        """
        Show user the results of the search (video title and URL).

        Args:
            results: a list of YouTube videos in order of relevance.
        """
        print("------------")
        for index, item in enumerate(results):
            if index >= 5:
                break
            print(f"\n{item[0]} \n- Score: {item[1]} \n"
                f"- Includes {item[2]}/{item[3]} keywords")

    def search_again(self):
        """
        Ask user if they want to make another search.

        Returns:
            user input (y/n) indicating if they want to search again
        """
        self.repeat = input("Do you want to search again? (y/n): ")
        return self.repeat