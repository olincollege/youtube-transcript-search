
import pytest
from view import ViewTerminal

view_test = ViewTerminal()

@pytest.mark.parametrize(
    ["available_channels", "inputs_list", "returns"],
    [
        # test standard user input
        (
            ["Kat Canavan"],                 # List of available channels
            ["Kat Canavan", "robots, nasa"], # Consecutive user inputs
            ("Kat Canavan", "robots, nasa")  # (channel, keywords) returned
        ),
        # test for spaces in channel input
        (
            ["Kat Canavan"],                  # List of available channels
            [" Kat Canavan ", "robots, nasa"] # Consecutive user inputs
            ("Kat Canavan", "robots, nasa")   # (channel, keywords) returned
        ),
        # asking for a channel that isn't downloaded
        (
            ["Kat Canavan"],                     # List of available channels
            ["Mark Rober", "y", "robots, nasa"], # Consecutive user inputs
            ("Mark Rober", "robots, nasa")       # (channel, keywords) returned
        ),
        # input wrong channel then input correct channel
        (
            ["Kat Canavan"],                     # List of available channels
            ["Cat Kanavan", "n", "Kat Canavan", "robots, nasa"], # user input
            ("Kat Canavan", "robots, nasa")    # (channel, keywords) returned
        ),
    ]
)

def test_get_search_input(monkeypatch, available_channels, inputs_list, returns):
    """_summary_

    Args:
        monkeypatch (_type_): _description_
        available_channels (list): _description_
        inputs_list (list): _description_
        returns (tuple of str): _description_
    """    

    inputs = iter(inputs_list)
    monkeypatch.setattr('builtins.input', lambda msg: next(inputs))
    assert view_test.get_search_input(available_channels) == returns

@pytest.mark.parametrize(
    # results should be a list of tuples (results is defined in model.py)
    # output should be the terminal output
    ["results", "output"],
    [
        # no results
        (
            [],                 # Should be a list of results tuples
            "------------\n"    # Text outputted to terminal
            "\n"
            "No results found."
        ),
        # results available
        (
            [('Mars Rover STEM Activity for Kids: https://www.youtube.com/watch?v=gnRV1TPTmDE', 54, 1, 1)],

            # text output in terminal
            "Results are scored by the total number of times keywords/ phrases"
            " appear in the transcript. The top scoring videos are:"
            "\n"
            "Mars Rover STEM Activity for Kids: https://www.youtube.com/watch?v=gnRV1TPTmDE"
            "\n"
            "- Score: 54"
            "\n"
            "- Includes 1/1 keywords"
        ),
    ]
)


def test_draw_results(capsys, results, output):
    """_summary_

    Args:
        capsys (_type_): _description_
        results (list of tuples): _description_
        output (str): _description_
    """    

    view_test.draw_results(results)
    assert capsys.readouterr().out.strip() == output



@pytest.mark.parametrize(
    ["inputs_list", "returns"],
    [
        (["y"], "y"),
        (["n"], "n"),
        (["hello", "y"], "y")
        (["qwerty", "n"], "n")
    ]
)

def test_search_again(monkeypatch, inputs_list, returns):
    """_summary_

    Args:
        monkeypatch (_type_): _description_
        inputs_list (list): _description_
        returns (str): _description_
    """    

    inputs = iter(inputs_list)
    monkeypatch.setattr('builtins.input', lambda msg: next(inputs))
    assert view_test.search_again() == returns