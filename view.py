
class YTSearchView():

    def __init__(self):
        self.draw_interface()
    
    def draw_interface(self):
        # Draw basic interface and allow user to input channel and keywords
        # self.chosen_channel = input("pick a channel: ")
        pass

    def draw_results(self, results):
        # Display URL/title results of search
        # print(results)
        pass


class ViewTerminal(YTSearchView):
    
    def __init__(self):
        self.draw_interface()
    
    def draw_interface(self):
        # Draw basic interface and allow user to input channel and keywords
        self.chosen_channel = input("pick a channel: ")

    def draw_results(self, results):
        # Display URL/title results of search
        print(results)