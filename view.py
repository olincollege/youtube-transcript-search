from abc import ABC

class View(ABC):

    def __init__(self):
        self.draw_interface()
    
    def draw_interface(self):
        """
        Display interface and prompt for user input
        """
        pass

    def get_search_input(self):
        """
        Get the channel and keywords from the user.
        """
        pass

    def draw_results(self, results):
        """
        Return the results of the search to the user

        Args:
            !results:
        """
        pass


class ViewTerminal(View):
    
    def __init__(self):
        self.draw_interface()
        self.get_search_input()
    
    def draw_interface(self):
        """
        Display interface
        """
        print("---YouTube transcript search---")
        print("Search every video on a YouTube channel for a keyword or words.")

    def get_search_input(self):
        """
        Get the channel and keywords from the user.
        """
        self.channel = 'CrashCourse' #! default for now

        print(\
        f"You are searching for videos on the YouTube channel {self.channel}")

        self.keywords = input("Enter comma separated keywords/phrases: ")

        print("Searching video transcripts...")

    def draw_results(self, results):
        # Display URL/title results of search

        # print URL and title

        print("------------")
        print(results)

    def search_again(self):
        again = input("Do you want to search again? (y/n): ")
        return again