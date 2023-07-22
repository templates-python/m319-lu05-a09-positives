import main


def test_while_1(capsys, monkeypatch):
    inputs = iter([0])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main_while()
    captured = capsys.readouterr()
    assert captured.out == 'The number is positive.\n'
