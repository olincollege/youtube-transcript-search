"""
Test functions for view.py
"""

import pytest
from view import ViewTerminal, search_again

view_test = ViewTerminal()


@pytest.mark.parametrize(
    ["available_channels", "inputs_list", "returns"],
    [
        # test standard user input
        (
            ["Kat Canavan"],                 # List of available channels
            ["Kat Canavan", "robots, nasa"],  # Consecutive user inputs
            ("Kat Canavan", "robots, nasa")  # (channel, keywords) returned
        ),

        # test for spaces in channel input
        (
            ["Kat Canavan"],                  # List of available channels
            [" Kat Canavan ", "robots, nasa"], # Consecutive user inputs
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

        # input 2 wrong channels then input correct channel
        (
            ["Kat Canavan"],                     # List of available channels
            ["Cat Kanavan", "n", "Kate Caravan","n", "Kat Canavan",
             "robots, nasa"], # user input
            ("Kat Canavan", "robots, nasa")    # (channel, keywords) returned
        ),

        # input wrong channel and "download"
        (
            ["Kat Canavan"],                      # List of available channels
            ["tralalalalalalalala", "y", "lala"], # user input
            ("tralalalalalalalala", "lala")      # (channel, keywords) returned
        ),
    ]
)
def test_get_search_input(monkeypatch, available_channels, inputs_list,
                          returns):
    """
    Tests view.get_search_input(), which collects user input for the channel
    and keywords to search.

    Args:
        monkeypatch (monkeypatch): monkeypatch
        available_channels (list): list of available channels (channels
            downloaded to disk). Serves as argument for get_search_input method.
        inputs_list (list): list of consecutive user inputs (strings). Will
            vary in length based on how long it takes the user to progress
            through the input tree.
        returns (tuple of str): expected return of function; should be a tuple
            with 2 strings, the channel name and keywords.
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
            [('Mars Rover STEM Activity for Kids: https://www.youtube.com/watc'
                'h?v=gnRV1TPTmDE', 54, 1, 1)],

            # text output in terminal
            # "------------\n"
            # "Results are scored by the total number of times keywords/ phrases"
            # " appear in the transcript. The top scoring videos are:"
            # "\n"
            # "\n"
            # "Mars Rover STEM Activity for Kids: https://www.youtube.com/watch?v=gnRV1TPTmDE "
            # "\n"
            # "- Score: 54 "
            # "\n"
            # "- Includes 1/1 keywords"

            '------------\n\nResults are scored by the total number of times keywords/ phrases appear in\n the transcript. The top scoring videos are: \n\n \n\n Mars Rover STEM Activity for Kids:\n https://www.youtube.com/watch?v=gnRV1TPTmDE \n\n - Score: 54\n\n - Includes 1/1 keywords'
        ),
    ]
)
def test_draw_results(capsys, results, output):
    """
    Tests view.draw_results(), which takes a list of results data and displays
    it to the user.

    Args:
        capsys (capsys): capsys
        results (list of tuples): A list of results tuples, passed into the
            function as an argument to be displayed.
        output (str): Expected output of the function. Should be a stylized
            version of the results data.
    """

    view_test.draw_results(results)
    assert capsys.readouterr().out.strip() == output


@pytest.mark.parametrize(
    ["inputs_list", "returns"],
    [
        (["y"], "y"),
        (["n"], "n"),
        (["hello", "y"], "y"),
        (["qwerty", "n"], "n")
    ]
)
def test_search_again(monkeypatch, inputs_list, returns):
    """
    Tests the function view.search_again(), which asks the user to decide
    whether they would like to run another search or end the session.

    Args:
        monkeypatch (monkeypatch): monkeypatch
        inputs_list (list): List of consecutive user inputs. Will vary in length
            based on how long it takes the user to reach a valid input.
        returns (str): Expected return, either "y" or "n".
    """

    inputs = iter(inputs_list)
    monkeypatch.setattr('builtins.input', lambda msg: next(inputs))
    assert search_again() == returns
