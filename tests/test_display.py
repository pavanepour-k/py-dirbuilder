from display.color import colorize

def test_colorize():
    result = colorize('test', 'red')
    assert isinstance(result, str)