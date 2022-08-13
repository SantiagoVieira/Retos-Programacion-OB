class Course():

    def __init__(self,id,name,teacher):
        self.id_course=id
        self.name_course = name
        self.teacher_course = teacher
        self.enrolled_students = []
        self.partials = []
    
    def remove_student(self,student):
        if student.name in self.enrolled_students:
            self.enrolled_students.remove(student.name)
            student.entolled_course.remove(self.name_course)
            print(f"{student.name} You have been successfully removed from the course {self.course_name}")

        else:
            print(f"{student.name} is not enrolled in the course {self.name_course}")
    
    def get_student_list(self):
        if self.enrolled_students:
            print(f"Students are",self.enrolled_students)
        else: 
            print(f"The course {self.enrolled_students} has no students ")    

class Partials():

    def __init__(self,course,name,porcentage,questions):
        self.name=name
        self.porcentage = porcentage
        self.questions = questions
        course.partials.append([self.name,self.porcentage,self.questions])

Math = Course("2","Math","Nestor")

class Teachers(Partials):

    def __init__(self,id,name,age):
        self.id=id
        self.age = age
        self.name = name
        self.charge = "Teacher"
        self.Courses=[]
        self.partials=[]

    def Newpartial(self,course,name,porcentage,questions):
        super().__init__(course,name,porcentage,questions)
        self.partials.append([course,name,porcentage,questions])

        
Nestor =Teachers("1a","Nestor alonso restrepo",25)
Nestor.Newpartial(Math,"Final",28,"1) 2+2=5? 2) Simon Bolivar es venezolano? 3) si el avion Vuela el aeroplano tambien? ")
print(Math.partials)

class Student():

    def __init__(self,id,name,age):
        self.id = id
        self.name = name.lower()
        self.age = age
        self.cargo= "Student"
        self.enrolled_course=[]
    
    def EnrolledCourse(self,course):
        self.enrolled_course.append(course)
        course.enrolled_students.append(self.name)

santiago = Student("3k","Santiago Vieira Ceballos",25)

santiago.EnrolledCourse(Math)
Math.get_student_list()
