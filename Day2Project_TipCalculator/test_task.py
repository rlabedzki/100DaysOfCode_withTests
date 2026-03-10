import pytest
from task import task

@pytest.mark.parametrize("bill, tip, people, expected_output", [    
    (100, 15, 4, "Welcome to the tip calculator!\n3.75"),
    (200, 10, 5, "Welcome to the tip calculator!\n4.0"), 
    (50, 12, 2, "Welcome to the tip calculator!\n3.0")
])

def test_task(monkeypatch, capsys, bill, tip, people, expected_output):
    inputs = iter([str(bill), str(tip), str(people)])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    task()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output