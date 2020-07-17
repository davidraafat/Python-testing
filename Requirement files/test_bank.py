import bank
from unittest import TestCase


#A test method should not depend on other test methods
class TestBankClass(TestCase):
    def setUp(self):
        self.test_object = bank.Bank(200)

    def test_credit_normal(self):
        self.test_object.credit(150)
        self.assertEqual(350, self.test_object.get_balance())
    def test_credit_none(self):
        with self.assertRaises(TypeError):
            self.test_object.credit(None)
        
    def test_credit_negative(self):  
        self.assertEqual(-1, self.test_object.credit(-150))

