import unittest
from sidamu_afoo_nltk.tokenize.tokenizer import Tokenizer

class TestTokenizer(unittest.TestCase):
    def setUp(self):
        """Set up the tokenizer object before each test."""
        self.tokenizer = Tokenizer()

    def test_word_tokenize(self):
        """Test word tokenization."""
        text = "Sidamu Afoo NLTK's tokenizer works!"
        expected = ['Sidamu', 'Afoo', 'NLTK', 's', 'tokenizer', 'works']
        result = self.tokenizer.word_tokenize(text)
        self.assertEqual(result, expected)

    def test_sentence_tokenize(self):
        """Test sentence tokenization."""
        text = "Sidamu Afoo is great. It works well!"
        expected = ['Sidamu Afoo is great', 'It works well']
        result = self.tokenizer.sentence_tokenize(text)
        self.assertEqual(result, expected)

    def test_tokenize(self):
        """Test tokenization method."""
        text = "Let's test the tokenizer functionality."
        expected_words = ['Let', 's', 'test', 'the', 'tokenizer', 'functionality']
        result_words = self.tokenizer.tokenize(text)
        self.assertEqual(result_words, expected_words)

        expected_sentences = ['Let', 's test the tokenizer functionality.']
        result_sentences = self.tokenizer.tokenize(text, by_sentence=True)
        self.assertEqual(result_sentences, expected_sentences)

if __name__ == "__main__":
    unittest.main()
