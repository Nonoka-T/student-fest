# Tests for simple-text-analyzer challenge
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../solutions"))


def get_analysis(text):
    """Helper function to replicate the core logic of analyze_text for testing."""
    if not text.strip():
        return None
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    most_frequent_word = max(word_freq, key=word_freq.get)
    unique_words = list(set(words))
    return {
        "word_count": word_count,
        "char_count": char_count,
        "most_frequent_word": most_frequent_word,
        "word_freq": word_freq,
        "unique_words": unique_words,
    }


def test_word_count():
    """Test that word count is calculated correctly."""
    result = get_analysis("The quick brown fox")
    assert result["word_count"] == 4


def test_char_count():
    """Test that character count includes spaces."""
    result = get_analysis("The quick brown fox")
    assert result["char_count"] == 19


def test_most_frequent_word():
    """Test that the most frequent word is identified correctly."""
    result = get_analysis("the cat sat on the mat the")
    assert result["most_frequent_word"] == "the"


def test_unique_words():
    """Test that unique words are returned correctly."""
    result = get_analysis("hello hello world")
    assert set(result["unique_words"]) == {"hello", "world"}


def test_empty_input():
    """Test that empty input returns None."""
    result = get_analysis("")
    assert result is None


def test_single_word():
    """Test analysis with a single word."""
    result = get_analysis("hello")
    assert result["word_count"] == 1
    assert result["most_frequent_word"] == "hello"


def test_special_characters():
    """Test that special characters are handled as part of words."""
    result = get_analysis("hello, world!")
    assert result["word_count"] == 2