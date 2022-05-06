
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
    model_test = YTSearchModel(parameters[0], parameters[1], parameters[2])

    assert model_test.channels.keys() == channels.keys()
    assert model_test.results == results

# def test_update_search(parameters, channels, results):
    # model_test = YTSearchModel(parameters[0], parameters[1], parameters[2])

    # assert model_test.
    # pass

# def test_search():
#     pass

