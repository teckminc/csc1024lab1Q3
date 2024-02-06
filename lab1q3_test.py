import lab1q3
from io import StringIO
from sys import stderr
def test_case1(monkeypatch, capsys):
    number_inputs = StringIO('30.5\n36.1\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab1q3.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'{1101.05}') != -1
    assert captured_stdout.strip().find(f'{133.2}') != -1