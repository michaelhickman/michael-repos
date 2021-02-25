"""test.py."""

import unittest
import number_to_words

class Test_number_to_words(unittest.TestCase):

    def test_get_words(self):
        self.assertEqual(number_to_words.get_words("000"), "")
        self.assertEqual(number_to_words.get_words("012"), "twelve")
        self.assertEqual(number_to_words.get_words("056"), "fifty-six")
        self.assertEqual(number_to_words.get_words("090"), "ninety")
        self.assertEqual(number_to_words.get_words("578"), "five hundred and seventy-eight")

    def test_convert(self):
        self.assertEqual(number_to_words.convert("536"), "five hundred and thirty-six")
        self.assertEqual(number_to_words.convert("9121"), "nine thousand, one hundred and twenty-one")
        self.assertEqual(number_to_words.convert("10022"), "ten thousand and twenty-two")
        self.assertEqual(number_to_words.convert("66723107008"), "sixty-six billion, seven hundred and twenty-three million, one hundred and seven thousand and eight")
        self.assertEqual(number_to_words.convert("50005"), "fifty thousand and five")
        self.assertEqual(number_to_words.convert("50050"), "fifty thousand and fifty")
        self.assertEqual(number_to_words.convert("50500"), "fifty thousand and five hundred")
        self.assertEqual(number_to_words.convert("50500"), "fifty thousand and five hundred")
        self.assertEqual(number_to_words.convert("500500"), "five hundred thousand and five hundred")
        self.assertEqual(number_to_words.convert("500000500000"), "five hundred billion and five hundred thousand")
        self.assertEqual(number_to_words.convert("500000500005"), "five hundred billion, five hundred thousand and five")


if __name__ == '__main__': 
    unittest.main()