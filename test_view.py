
import pytest
from view import ViewTerminal

view_test = ViewTerminal()



def test_get_search_input():
    pass

@pytest.mark.parametrize(
    # results should be a list of tuples (results is defined in model.py)
    # output should be the terminal output
    ["results", "output"],
    [
        ("", "------------\n"
             "\n"
             "No results found.")
    ]
)

def test_draw_results(capsys, results, output):
    
    view_test.draw_results(results)
    assert capsys.readouterr().out.strip() == output



@pytest.mark.parametrize(
    ["inputs_list", "end_result"],
    [
        (["y"], "y"),
        (["n"], "n"),
        (["hello", "y"], "y")
    ]
)

def test_search_again(monkeypatch, inputs_list, end_result):

    inputs = iter(inputs_list)
    monkeypatch.setattr('builtins.input', lambda msg: next(inputs))
    assert view_test.search_again() == end_result