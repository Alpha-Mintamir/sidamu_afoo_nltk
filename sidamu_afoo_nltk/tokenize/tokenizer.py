import re
import string

class Tokenizer:
    def __init__(self):
        """Initialize the Tokenizer with necessary configurations."""
        self.punctuation = string.punctuation

    def clean_text(self, text: str) -> str:
        """Clean the text by removing unwanted characters."""
        # Remove non-UTF-8 characters and unnecessary spaces
        text = re.sub(r'[^\x00-\x7F]+', '', text)
        text = text.strip()
        return text

    def word_tokenize(self, text: str) -> list:
        """Tokenize the input text into words, removing punctuation."""
        # Clean the text before tokenizing
        text = self.clean_text(text)
        # Tokenize using regex to split based on whitespace and punctuation
        tokens = re.findall(r'\b\w+\b', text)
        return tokens

    def sentence_tokenize(self, text: str) -> list:
        """Tokenize the input text into sentences."""
        # Split the text into sentences using regex.
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
        return [sentence.strip() for sentence in sentences]

    def tokenize(self, text: str, by_sentence=False) -> list:
        """Main method to tokenize text. Can return tokens by sentence or word."""
        if by_sentence:
            return self.sentence_tokenize(text)
        else:
            return self.word_tokenize(text)

    def __repr__(self):
        return f"Tokenizer(punctuation={self.punctuation})"


# Example usage:
if __name__ == "__main__":
    tokenizer = Tokenizer()
    sample_text = "Hello, world! This is Sidamu Afoo NLTK's tokenizer. Let's tokenize this text."
    
    # Tokenize by words
    print("Word Tokens:", tokenizer.tokenize(sample_text))
    
    # Tokenize by sentences
    print("Sentence Tokens:", tokenizer.tokenize(sample_text, by_sentence=True))
 
