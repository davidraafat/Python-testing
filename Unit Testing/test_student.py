import student
from unittest import TestCase


#A test method should not depend on other test methods
class TestStudentClass(TestCase):
    def setUp(self):
        self.test_object = student.Student('Ahmed', ["Software Engineering", "Compilers"])

    def test_add_course(self):
        self.test_object.add_course("Arch")
        self.assertIn('Arch', self.test_object.get_courses())

    def test_get_credit_hours(self):
        self.assertEqual(self.test_object.get_credit_hours(), 4)
