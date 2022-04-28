
class YTSearchView():

    def __init__(self):
        self.draw_interface()
    
    def draw_interface(self):
        """
        Display interface and prompt for user input
        """

        # Draw basic interface and allow user to input channel and keywords
        pass

    def draw_results(self, results):
        """
        Return the results of the search to the user

        Args:
            !results:
        """
        pass


class ViewTerminal(YTSearchView):
    
    def __init__(self):
        self.draw_interface()
    
    def draw_interface(self):
        """
        Display interface and prompt for user input
        """
        self.chosen_channel = 'CrashCourse' #! default for now
        # self.chosen_channel = \
        # input("What YouTube channel would you like to search?: )

        self.keywords = input("Enter comma separated keywords/ phrases: ")


    def draw_results(self, results):
        # Display URL/title results of search

        # print URL and title
        print(results)