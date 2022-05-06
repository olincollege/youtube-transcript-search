
import pytest
from view import ViewTerminal

view_test = ViewTerminal()



def test_get_search_input():
    pass

def test_draw_results():
    pass



@pytest.mark.parametrize(
    ["inputs_list", "end_result"],
    [
        (["y"], "y"),
        (["n"], "n"),
        (["hello", "y"], "y")
        (["qwerty", "n"], "n")
    ]
)

def test_search_again(monkeypatch, inputs_list, end_result):

    inputs = iter(inputs_list)
    monkeypatch.setattr('builtins.input', lambda msg: next(inputs))
    assert view_test.search_again() == end_result