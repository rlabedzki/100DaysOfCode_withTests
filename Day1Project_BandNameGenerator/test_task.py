import pytest
from task import band_name_generator

@pytest.mark.parametrize("city, pet, expected_output", [
    ("Londyn", "Reks", "Welcome to the Band Name Generator.\nBand name could be Londyn Reks"),
    ("New York", "Fluffy", "Welcome to the Band Name Generator.\nBand name could be New York Fluffy"),
    ("Paris", "Whiskers", "Welcome to the Band Name Generator.\nBand name could be Paris Whiskers"),
])

def test_band_name(monkeypatch, capsys, city, pet, expected_output):
    # add the inputs to the function using monkeypatch
    # capsys is used to capture the output of the function
    # these are pytest fixtures injected by pytest when the test is run
    inputs = iter([city, pet]) # create an iterator with the inputs we want to provide to the function
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    # with every call for input, the next value from the inputs iterator will be returned
    
    band_name_generator()  # function prints the output, we will capture it using capsys
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output