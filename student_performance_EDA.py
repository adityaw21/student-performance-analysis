# student-performance-analysis
Python project analyzing student performance data using Pandas and Matplotib
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("student_performance.csv")

print("----- Student Performance Dataset -----")
print(data.head(), "\n")

print("----- Missing Values -----")
print(data.isnull().sum(), "\n")

print("----- Statistical Summary -----")
print(data.describe(), "\n")

plt.figure()
plt.scatter(data["StudyHours"], data["Marks"])
plt.title("Relationship Between Study Hours and Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

attendance_avg = data.groupby("Attendance")["Marks"].mean()
plt.figure()
attendance_avg.plot(kind="bar")
plt.title("Average Marks Based on Attendance Levels")
plt.xlabel("Attendance Level")
plt.ylabel("Average Marks")
plt.show()

parent_edu_avg = data.groupby("ParentEducation")["Marks"].mean().sort_values()
plt.figure()
parent_edu_avg.plot(kind="bar")
plt.title("Parent Education Background vs Average Student Marks")
plt.xlabel("Parent Education Level")
plt.ylabel("Average Marks")
plt.show()

print("Analysis completed successfully!")
