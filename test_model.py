
import pytest
from model import Video, Channel, YTSearchModel

# Developer's note: the following tests check for search functionality, not
# downloading files or checking for available channels as results will vary
# per user and machine.

@pytest.mark.parametrize(
    # parameters = [current_channel_name, keywords, available_channels]
    ["parameters", "channels", "results"],
    [
        # standard search with single key and single result
        (
            [
                "Kat Canavan",      # Current channel name
                "nasa",             # Keyword
                ["Kat Canavan"]     # Available channels (list)
            ],
            {                       # Dictionary of channel objects
                "Kat Canavan": Channel("Kat Canavan"),# Only using keys for test
            },
            [ # List of results tuples
                ("Mars Rover STEM Activity for Kids: https://www.youtube.com/watch?v=gnRV1TPTmDE", 6, 1, 1),
            ]
        ),

        # standard search with single key and multiple results
        (
            [
                "Kat Canavan",      # Current channel name
                "marble",           # Keyword
                ["Kat Canavan"]     # Available channels (list)
            ],
            {                       # Dictionary of channel objects
                "Kat Canavan": Channel("Kat Canavan"),# Only using keys for test
            },
            [ # List of results tuples
                ("Paper Roller Coaster Tutorial: https://www.youtube.com/watch?v=dFnBrWlyhvE", 16, 1, 1), ("Paper Roller Coaster Marblelympics Parody: https://www.youtube.com/watch?v=0YowfCy-xcQ", 12, 1, 1)
            ]
        ),

        # standard search with multiple keys and multiple results
        (
            [
                "Kat Canavan",      # Current channel name
                "test, robot",      # Keywords
                ["Kat Canavan"]     # Available channels (list)
            ],
            {                       # Dictionary of channel objects
                "Kat Canavan": Channel("Kat Canavan"),# Only using keys for test
            },
            [ # List of results tuples
                ("Teaching an AI the Difference Between Apples and Bananas: https://www.youtube.com/watch?v=XEjS_FDSsvo", 14, 2, 2), ("Mars Rover STEM Activity for Kids: https://www.youtube.com/watch?v=gnRV1TPTmDE", 8, 2, 2), ("Paper Roller Coaster Tutorial: https://www.youtube.com/watch?v=dFnBrWlyhvE", 6, 1, 2), ("Paper Roller Coaster Marblelympics Parody: https://www.youtube.com/watch?v=0YowfCy-xcQ", 4, 1, 2)
            ]
        ),

        # no results
        (
            [
                "Kat Canavan",      # Current channel name
                "this sentence is not said in any videos.", # Keywords
                ["Kat Canavan"]     # Available channels (list)
            ],
            {                       # Dictionary of channel objects
                "Kat Canavan": Channel("Kat Canavan"),# Only using keys for test
            },
            [ # List of results tuples

            ]
        ),

        # The next three tests should all have the same results.

        # Lowercase search
        (
            [
                "Kat Canavan",      # Current channel name
                "banana",           # Keyword
                ["Kat Canavan"]     # Available channels (list)
            ],
            {                       # Dictionary of channel objects
                "Kat Canavan": Channel("Kat Canavan"),# Only using keys for test
            },
            [ # List of results tuples
                ("Teaching an AI the Difference Between Apples and Bananas: https://www.youtube.com/watch?v=XEjS_FDSsvo", 15, 1, 1)
            ]
        ),

        # Title-case search
        (
            [
                "Kat Canavan",      # Current channel name
                "Banana",           # Keyword
                ["Kat Canavan"]     # Available channels (list)
            ],
            {                       # Dictionary of channel objects
                "Kat Canavan": Channel("Kat Canavan"),# Only using keys for test
            },
            [ # List of results tuples
                ("Teaching an AI the Difference Between Apples and Bananas: https://www.youtube.com/watch?v=XEjS_FDSsvo", 15, 1, 1)
            ]
        ),

        # Uppercase search
        (
            [
                    "Kat Canavan",      # Current channel name
                    "BANANA",           # Keyword
                    ["Kat Canavan"]     # Available channels (list)
                ],
                {                       # Dictionary of channel objects
                    "Kat Canavan": Channel("Kat Canavan"),# Only using keys for test
                },
                [ # List of results tuples
                    ("Teaching an AI the Difference Between Apples and Bananas: https://www.youtube.com/watch?v=XEjS_FDSsvo", 15, 1, 1)
                ]
        ),
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

