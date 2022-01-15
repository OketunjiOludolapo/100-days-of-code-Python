student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}


student_grades={}

for name in student_scores:
    if student_scores[name]>90:
        student_grades[name]="Outstanding"
    elif student_scores[name]>=80:
        student_grades[name]="Excellent"
    elif student_scores[name]>=70:
        student_grades[name]="Brilliant"
    else:
        student_grades[name]="You can do better"
# 🚨 Don't change the code below 👇
print(student_grades)