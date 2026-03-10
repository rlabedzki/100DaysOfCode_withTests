import pytest
from task import game

@pytest.mark.parametrize("move0, move1, move2, expected_output", [    
    ("right", "", "" ,"Welcome to Treasure Island.\nYour mission is to find the treasure.\nDragon eats you, game over."),
    ("left", "wait", "yellow", "Welcome to Treasure Island.\nYour mission is to find the treasure.\nYou win"),
    ("left", "wait", "red", "Welcome to Treasure Island.\nYour mission is to find the treasure.\nBurned by fire, game over"),
    ("left", "wait", "blue", "Welcome to Treasure Island.\nYour mission is to find the treasure.\nBeats eat you, game over"),
    ("left", "wait", "green", "Welcome to Treasure Island.\nYour mission is to find the treasure.\nGame over"),
    ("left", "swim", "", "Welcome to Treasure Island.\nYour mission is to find the treasure.\nCrocodile eats you, game over.")
])

def test_task(monkeypatch, capsys, move0, move1, move2, expected_output):
    inputs = iter([move0, move1, move2])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    game()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output