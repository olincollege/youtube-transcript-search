
import pytest
from view import ViewTerminal

view_test = ViewTerminal()

@pytest.mark.parametrize(
    ["available_channels", "inputs_list", "returns"],
    [
        (
            ["Kat Canavan"],                 # List of available channels
            ["Kat Canavan", "robots, nasa"], # Consecutive user inputs
            ("Kat Canavan", "robots, nasa")  # (channel, keywords) returned
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
        (
            [],                 # Should be a list of results tuples
            "------------\n"    # Text outputted to terminal
            "\n"
            "No results found."
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