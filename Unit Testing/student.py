
class Student():
    def __init__(self,name,courses):
    
        self.name=str(name)
        self.courses=courses

    def add_course(self,course):
        self.courses.append(course)
    
    def get_courses(self):
        return self.courses
    
    def get_credit_hours(self):
        return len(self.courses)*2
    
            
        
        
        

