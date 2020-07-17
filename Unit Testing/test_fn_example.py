from unittest import TestCase
def start_with_same_letter(first_string,second_string):
    try:
        if first_string[0]==second_string[0]:
            return 
        return False
    except:
        raise TypeError


class TestStartWithSameLetterFn(TestCase):
    def test_different_first_letter(self):
        self.assertFalse(start_with_same_letter("hello", "world"))

    def test_same_first_letter(self):
        self.assertTrue(start_with_same_letter("hello", "hi"))

    def test_none_parameter(self):
        with self.assertRaises(TypeError):
            start_with_same_letter("hello", None)