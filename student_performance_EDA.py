import pandas as pd
import matplotlib.pyplot as plt

student_data = pd.read_csv("student_performance.csv")

print("Student Performance Dataset Preview")
print(student_data.head(), "\n")

print("Missing Values in Dataset")
print(student_data.isnull().sum(), "\n")

print("Statistical Summary of Dataset")
print(student_data.describe(), "\n")

plt.figure()
plt.scatter(student_data["StudyHours"], student_data["Marks"], color="blue")
plt.title("Effect of Study Hours on Student Exam Marks")
plt.xlabel("Number of Study Hours")
plt.ylabel("Final Exam Marks")
plt.grid(True)
plt.show()

average_marks_by_attendance = student_data.groupby("Attendance")["Marks"].mean()
plt.figure()
average_marks_by_attendance.plot(kind="bar", color="green")
plt.title("Average Exam Marks by Attendance Level")
plt.xlabel("Attendance Level")
plt.ylabel("Average Marks")
plt.grid(axis="y")
plt.show()

average_marks_by_parent_edu = student_data.groupby("ParentEducation")["Marks"].mean().sort_values()
plt.figure()
average_marks_by_parent_edu.plot(kind="bar", color="orange")
plt.title("Impact of Parental Education on Student Exam Marks")
plt.xlabel("Parent Education Level")
plt.ylabel("Average Marks")
plt.grid(axis="y")
plt.show()

print("Analysis completed successfully!")
