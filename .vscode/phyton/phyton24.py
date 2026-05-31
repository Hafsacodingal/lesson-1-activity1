#Class Student
class student:
    grade=10
    print("Hi I am a student of grade",grade)
ob=student()
#Class Student-2
class student:
    grade=10
    name="Hafsa"
    def introduction(self):
        print("Hi I am a student")
    def details(self):
        print("My name is",self.name)
        print("I study in Grade",self.grade)
ob=student()
ob.introduction()
ob.details()
