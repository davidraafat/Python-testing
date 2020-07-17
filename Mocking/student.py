class DataProvider():#declaration of the class that needs to be mocked
   def get_student_courses(self,student_id):
       pass

class Student():#class that needs to be tested
    def __init__(self,name,id,data_accessor:DataProvider):
    
        self.name=str(name)
        self.id=id
        self.data_accessor=data_accessor
    
    def get_credit_hours(self):
        course_list=self.data_accessor.get_student_courses(self.id)['courses']
        credit_hours=0
        for course in course_list:
            credit_hours+=course['hours']
        return credit_hours

        
# course structure: dictionnary with id and hours