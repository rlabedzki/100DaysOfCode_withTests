import  task

def test_play_correctly_handles_valid_inputs(monkeypatch, capsys):
    inputs = iter(['0', '1', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    task.play()
    captured = capsys.readouterr()
    assert (
        captured.out.strip().find("You win!") != -1
        or captured.out.strip().find("It's a draw!") != -1
        or captured.out.strip().find("You loose!") != -1
    )

def test_play_correctly_handles_invalid_input(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: '4')
    task.play()
    captured = capsys.readouterr()
    assert captured.out.strip() == "You choose poorly!"