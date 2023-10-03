import main


def test_while_1(capsys, monkeypatch):
    inputs = iter(['0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main_while()
    captured = capsys.readouterr()
    assert captured.out == ''


def test_while_2(capsys, monkeypatch):
    inputs = iter(['4', '-3', '0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main_while()
    captured = capsys.readouterr()
    assert captured.out == '16\nUnsuitable number\n'


def test_break_1(capsys, monkeypatch):
    inputs = iter(['0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main_while()
    captured = capsys.readouterr()
    assert captured.out == ''


def test_break_2(capsys, monkeypatch):
    inputs = iter(['4', '-3', '0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main_while()
    captured = capsys.readouterr()
    assert captured.out == '16\nUnsuitable number\n'


def test_continue_1(capsys, monkeypatch):
    inputs = iter(['0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main_while()
    captured = capsys.readouterr()
    assert captured.out == ''


def test_continue_2(capsys, monkeypatch):
    inputs = iter(['4', '-3', '0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main_while()
    captured = capsys.readouterr()
    assert captured.out == '16\nUnsuitable number\n'
