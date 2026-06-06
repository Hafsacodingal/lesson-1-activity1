student = ("Hafsa", 10, "Grade 5")
print("Student:", student[0])
print("Roll No:", student[1])

monday = {"Math", "English", "Science"}
tuesday = {"Math", "Urdu", "Art"}

print("\nMonday subjects:", monday)
print("Tuesday subjects:", tuesday)

common = monday & tuesday 
all_subjects = monday | tuesday 
only_monday = monday - tuesday 

print("\nCommon subjects:", common)
print("All subjects:", all_subjects)
print("Only Monday:", only_monday)

monday.add("PE")
print("\nAfter adding PE to Monday:", monday)