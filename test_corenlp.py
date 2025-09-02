from nlplogic.corenlp import get_phrases


def test_get_phrase():
    assert "chemax municipality" in get_phrases("chemax")
