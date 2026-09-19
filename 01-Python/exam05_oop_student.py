
class Student:
    def __init__(self, name , score):
        self.name = name
        self.score = score

    def check_result(self):
        if self.score >= 10 :
            print("قبول شد" , self.name)
        else:
            print(" رد شد",self.name )

student1 = Student("Reza", 18)
student2 = Student("Ali", 8)

student1.check_result()
student2.check_result()