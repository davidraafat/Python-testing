from student import DataProvider,Student
from unittest import TestCase

class MockDataProvider(DataProvider):#mock 
    def get_student_courses(self,student_id):
        return {'courses':[{'id':'CMP203','hours':3},{'id':'CMP111','hours':2}]}


class TestClient(TestCase):
    def setUp(self):
        self.student=Student("Ahmed",11,MockDataProvider())
    
    def test_get_credit_hours(self):
        self.assertEqual( self.student.get_credit_hours(),5)


    

