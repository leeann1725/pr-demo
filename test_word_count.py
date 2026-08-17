from word_count import count_words


def test_counts_simple_sentence():
    assert count_words("the cat sat on the mat") == {
        "the": 2,
        "cat": 1,
        "sat": 1,
        "on": 1,
        "mat": 1,
    }


def test_is_case_insensitive():
    assert count_words("Cat cat CAT") == {"cat": 3}


def test_strips_punctuation():
    assert count_words("Hello, world! Hello.") == {"hello": 2, "world": 1}


def test_empty_string_returns_empty_dict():
    assert count_words("") == {}
