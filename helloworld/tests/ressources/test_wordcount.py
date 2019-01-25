"""tests for wordcount.py."""

from unittest import TestCase
from unittest.mock import MagicMock

from helloworld.ressources.wordcount import Wordcount


class TestWordcount(TestCase):
    """Test for Wordcount endpoint."""

    def test_get(self):
        """Test tokenize endpoint with mocked tokenize logic."""
        testee = Wordcount()
        testee.tokenize = MagicMock(return_value=['hello', 'world', 'bla'])
        self.assertEqual(testee.get('hello world'), {'wordcount': 3})
        testee.tokenize.assert_called_with = 'hello world'

    def test_tokenize_single_word(self):
        """Test the tokenize method."""
        testee = Wordcount()
        self.assertEqual(testee.tokenize("one"), ['one'])

    def test_tokenize_empty(self):
        """Test the tokenize method."""
        testee = Wordcount()
        self.assertEqual(testee.tokenize(None), [])

    def test_tokenize_multiple(self):
        """Test the tokenize method."""
        testee = Wordcount()
        self.assertEqual(testee.tokenize("one two three"),
                         ['one', 'two', 'three'])
