import matplotlib.pyplot as plt

# Sample data
students = ["A", "B", "C", "D", "E"]
marks = [75, 85, 65, 90, 80]

# 1. Scatter Plot
plt.scatter(students, marks)
plt.title("Student Marks - Scatter Plot")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 2. Bar Chart
plt.bar(students, marks)
plt.title("Student Marks - Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 3. Line Chart
plt.plot(students, marks, marker="o")
plt.title("Student Marks - Line Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()