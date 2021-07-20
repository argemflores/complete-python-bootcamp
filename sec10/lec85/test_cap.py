# import unittest library and the script to test
import unittest
import cap

# create a class for the test case
class TestCap(unittest.TestCase):
    # test capitalizing one word only
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        # check whether actual and expected results are equal
        self.assertEqual(result, 'Python')
    
    # test capitalizing two or more words
    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        # check whether actual and expected results are equal
        self.assertEqual(result, 'Monty Python')

if __name__ == '__main__':
    unittest.main()
