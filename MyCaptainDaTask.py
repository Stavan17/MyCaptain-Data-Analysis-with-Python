import numpy as np
import matplotlib.pyplot as plt
data = {'Professional Communication' : 72, 'Engineering Mathematics - 1' : 69, 'Engineering Chemistry' : 87, 'Problem Solving and Programming' : 88, 'Engineering Physics' : 74, 'Engineering Chemistry Lab' : 87, 'Problem Solving and Programming Lab' : 98, 'Engineering Physics Lab' : 85, 'Leadership Development' : 91}
Course_Name = list(data.keys())
Marks_Received = list(data.values())
fig =plt.figure(figsize = (10, 5))
plt.bar(Course_Name, Marks_Received, color = 'red', width = 0.5)
plt.xlabel = ("Course Name")
plt.ylabel = ("Marks Received")
plt.title = ("1st Semester Marks")
plt.xticks(rotation=30,ha='right')
plt.tight_layout()
plt.show()