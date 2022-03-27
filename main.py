class Student:
    amount_of_student=0
    def __init__(self, heiqth=160):
        self.heiqth=heiqth
        Student.amount_of_student+=1
    def grow(self, heiqth=1):
        self.heiqth+=heiqth
nick=Student()
kate=Student(heiqth=170)
nick.grow(heiqth=15)
print(kate.heiqth)
print(nick.heiqth)