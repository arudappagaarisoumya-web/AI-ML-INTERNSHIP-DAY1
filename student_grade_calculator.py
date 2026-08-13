# Student Grade Calculator

print("===== Student Grade Calculator =====")
name = input("Enter student name: ")
maths = float(input("Enter Maths marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))
python = float(input("Enter Python marks: "))
dbms = float(input("Enter DBMS marks: "))
total = maths + science + english + python + dbms
average = total / 5

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"
print("\n===== Result =====")
print("Student Name:", name)
print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)