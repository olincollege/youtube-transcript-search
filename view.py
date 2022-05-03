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
                print("\nThe channels that are currently available to search"
                " are:")
                for channel in available_channels:
                    print(" | " + channel)

                print("\n(You can also add a new channel by entering the exact"
                " channel name below)")

                channel = input("\nWhich channel would you like to search? ")\
                    .strip() # remove unwanted spaces

                # if the channel is not already downloaded locally, confirm that
                # the user would like to download it.
                if channel not in available_channels:
                    input_val = ""
                    while input_val != "y" and input_val != "n":
                        input_val = input("\nThis channel will need to be "
                        "locally downloaded and the search will take longer"
                        " than usual, would you like to continue? (y/n): ")

                    if input_val == "y": # yes
                    # update search message to reflect increased loading time
                        search_message = ("Downloading transcript data and"
                        " searching video transcripts. This may take a few"
                        " minutes...")
                        break
                else: # channel is available
                    break

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
        # indicate if the search returned no results
        if len(results) == 0:
            print("\nNo results found.\n")
        # display the top search results
        else:
            print("Results are scored by the total number of times keywords/"
            " phrases appear in the transcript. The top scoring videos are: ")
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
        self.repeat = ""
        while self.repeat != "y" and self.repeat != "n":
            self.repeat = input("Do you want to search again? (y/n): ")
        return self.repeat

    def error(self, error_code=0):
        """
        Indicate to the user that an error has occurred.

        Args:
            error_code: an int (default of 0) indicates what the error is
        """
        # default error message
        if error_code == 0:
            print("\n------------\nERROR\n------------")

        # channel fails to download
        if error_code == 1:
            print("\n------------\nERROR DOWNLOADING TRANSCRIPTS. CHANNEL NAME" " MAY BE INCORRECT.\n\n(Hint: make sure the channel is spelled"
            " correctly and spaces/capital letters are right)\n------------")
