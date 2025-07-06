import unittest

def unique_morse_words(words):
    # Morse code mapping for a-z
    morse_map = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
        'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
        'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
        'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
        'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'
    }
    
    # Convert each word to its Morse code and store in a set
    morse_codes = set()
    for word in words:
        morse = ''.join(morse_map[char] for char in word)
        morse_codes.add(morse)
    
    # Return the number of unique Morse codes
    return len(morse_codes)

class TestUniqueMorseWords(unittest.TestCase):
    def test_duplicate_morse_codes(self):
        """Test case where words map to distinct Morse codes"""
        self.assertEqual(unique_morse_words(["cat", "act", "dog"]), 3)  # Updated to expect 3
    
    def test_identical_words(self):
        """Test case where words are identical"""
        self.assertEqual(unique_morse_words(["hello", "hello"]), 1)
    
    def test_distinct_morse_codes(self):
        """Test case where all words have different Morse codes"""
        self.assertEqual(unique_morse_words(["a", "b"]), 2)
    
    def test_single_word(self):
        """Test case with a single word"""
        self.assertEqual(unique_morse_words(["code"]), 1)
    
    def test_empty_word_list(self):
        """Test case with an empty list of words"""
        self.assertEqual(unique_morse_words([]), 0)

if __name__ == '__main__':
    unittest.main()