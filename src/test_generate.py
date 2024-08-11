import unittest
from generate import extract_title

class TestGenerate(unittest.TestCase):
    def test_generate(self):
        md = '# Hello'
        result = extract_title(md)
        self.assertEqual(result, 'Hello')

    # def test_exception_generate(self):
    #     md = '## Hello'
    #     with self.assertRaises(Exception) as context:
    #         extract_title(md)
    #     self.assertEqual(str(context.exception), 'no h1 header')

if __name__ == '__main__':
    unittest.main()