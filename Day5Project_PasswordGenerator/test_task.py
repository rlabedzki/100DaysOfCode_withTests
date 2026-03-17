import task
import pytest

@pytest.mark.parametrize("letters, symbols, numbers", [    
    (4, 2, 3),
    (200, 10, 5), 
    (50, 12, 2)
])

def test_generate_password(monkeypatch, capsys, letters, symbols, numbers):
    inputs = iter([str(letters), str(symbols), str(numbers)])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    task.generate_password()
    captured = capsys.readouterr()
    captured_password = captured.out.strip().split('\n')[-1]
    assert len(captured_password) == letters + symbols + numbers
    assert sum(c.isalpha() for c in captured_password) == letters
    assert sum(c in task.symbols for c in captured_password) == symbols
    assert sum(c in task.numbers for c in captured_password) == numbers