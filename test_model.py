
import pytest
from model import Video, Channel, YTSearchModel

@pytest.mark.parametrize(
    # parameters = [current_channel_name, keywords, available_channels]
    ["parameters", "channels", "results"],
    [
        (
            [
                "Kat Canavan",      # Current channel name
                "robots, nasa",     # Keywords
                ["Kat Canavan"]     # Available channels (list)
            ],
            {                       # Dictionary of channel objects
                "Kat Canavan": Channel("Kat Canavan"),# Only using keys for test
            },
            [                       # List of results tuples
                (),
            ]
        )
    ]
)

def test_YTSearchModel_init(parameters, channels, results):
    """
    Tests model.__init__(), which takes 3 arguments and updates a dictionary of
    channels that are in program memory, along with a list of search results.

    Args:
        parameters (list): Includes two strings and a list, representing the 3
            arguments taken by the function: current_channel_name, keywords, and
            available_channels.
        channels (dict): Expected value of model.channels, dictionary with keys
            as channel names of channels loaded into memory, with values as
            corresponding channel objects.
        results (tuple): Expected value of model.results, tuple including video
            title+url (str), count of keywords in transcript, number of unique
            keywords in transcript, and total number of searched keywords.
    """

    model_test = YTSearchModel(parameters[0], parameters[1], parameters[2])

    assert model_test.channels.keys() == channels.keys()
    assert model_test.results == results

# def test_update_search(parameters, channels, results):
    # model_test = YTSearchModel(parameters[0], parameters[1], parameters[2])

    # assert model_test.
    # pass

# def test_search():
#     pass

