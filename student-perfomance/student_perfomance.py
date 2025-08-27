# student_performance.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsPerformance.csv')  # upload file
sns.boxplot(x='gender', y='math score', data=df)
plt.title('Math score by gender')
plt.tight_layout()
plt.savefig('student-performance/math_by_gender.png')
print("Saved plot to student-performance/math_by_gender.png")
