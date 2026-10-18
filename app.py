"""
Project: Student Performance Analysis
Description: Analyze students' study hours and exam scores using
             statistical summaries and data visualizations.

Libraries: pandas, matplotlib, seaborn
""" 
# ============================================================
# 1. IMPORT LIBRARIES
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# 2. SET VISUALIZATION STYLE
# ============================================================

sns.set_theme(style="whitegrid", palette="viridis")

plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["axes.titlesize"] = 15
plt.rcParams["axes.labelsize"] = 12
plt.rcParams["xtick.labelsize"] = 10
plt.rcParams["ytick.labelsize"] = 10

# ============================================================
# 3. CREATE THE DATASET
# ============================================================

data = {
    "Student": [
        "Ali", "Sara", "Ahmed", "Ayesha", "Usman",
        "Fatima", "Hamza", "Zainab", "Bilal", "Hira"
    ],
    "Study_Hours": [2, 5, 3, 7, 4, 6, 1, 8, 3, 5],
    "Exam_Score": [45, 78, 55, 90, 65, 85, 35, 95, 60, 80]
}

df = pd.DataFrame(data)

# ============================================================
# 4. CATEGORIZE STUDENT PERFORMANCE
# ============================================================

def categorize_performance(score):
    """Assign a performance category based on the exam score."""

    if score >= 80:
        return "Excellent"
    elif score >= 60:
        return "Good"
    else:
        return "Needs Improvement"

df["Performance"] = df["Exam_Score"].apply(categorize_performance)

# ============================================================
# 5. DISPLAY DATASET AND STATISTICS
# ============================================================

print("\n" + "=" * 55)
print("          STUDENT PERFORMANCE ANALYSIS")
print("=" * 55)

print("\n1. STUDENT DATASET")
print("-" * 55)
print(df.to_string(index=False))

print("\n2. SUMMARY STATISTICS")
print("-" * 55)

print(f"Total Students       : {len(df)}")
print(f"Average Exam Score   : {df['Exam_Score'].mean():.2f}")
print(f"Highest Exam Score   : {df['Exam_Score'].max()}")
print(f"Lowest Exam Score    : {df['Exam_Score'].min()}")
print(f"Average Study Hours  : {df['Study_Hours'].mean():.2f}")

top_student = df.loc[df["Exam_Score"].idxmax()]
lowest_student = df.loc[df["Exam_Score"].idxmin()]

print(f"Highest Scorer       : {top_student['Student']}")
print(f"Lowest Scorer        : {lowest_student['Student']}")

print("\n3. PERFORMANCE DISTRIBUTION")
print("-" * 55)
print(df["Performance"].value_counts().to_string())

print("\n4. KEY INSIGHTS")
print("-" * 55)

correlation = df["Study_Hours"].corr(df["Exam_Score"])

print(
    f"1. The average exam score is "
    f"{df['Exam_Score'].mean():.2f}."
)

print(
    f"2. {top_student['Student']} achieved the highest score "
    f"of {top_student['Exam_Score']}."
)

print(
    f"3. {lowest_student['Student']} achieved the lowest score "
    f"of {lowest_student['Exam_Score']}."
)

print(
    f"4. The correlation between study hours and exam scores "
    f"is {correlation:.2f}, indicating a very strong positive "
    f"linear relationship in this dataset."
)

print(
    "5. Students who studied longer generally achieved "
    "higher exam scores in this sample."
)

print(
    "6. Correlation does not prove causation. Other factors, "
    "such as prior knowledge and study methods, may also "
    "influence exam performance."
)

# ============================================================
# 6. VISUALIZATION 1: STUDY HOURS VS EXAM SCORES
# ============================================================

plt.figure()

sns.scatterplot(
    data=df,
    x="Study_Hours",
    y="Exam_Score",
    hue="Performance",
    s=120
)

plt.title("Study Hours vs Exam Scores", pad=15)
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.legend(title="Performance")
plt.tight_layout()
plt.show()

# ============================================================
# 7. VISUALIZATION 2: EXAM SCORES BY STUDENT
# ============================================================

plt.figure(figsize=(10, 6))

sns.barplot(
    data=df,
    x="Student",
    y="Exam_Score",
)

plt.title("Exam Scores by Student", pad=20)
plt.xlabel("Student", labelpad=15)
plt.ylabel("Exam Score", labelpad=10)
plt.ylim(0, 100)

plt.xticks(rotation=45, ha="right")
plt.tight_layout(pad=2)

plt.show()

# ============================================================
# 8. VISUALIZATION 3: DISTRIBUTION OF EXAM SCORES
# ============================================================

plt.figure()

sns.histplot(
    data=df,
    x="Exam_Score",
    bins=6,
    kde=True
)

plt.title("Distribution of Exam Scores", pad=15)
plt.xlabel("Exam Score")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()

# ============================================================
# 9. VISUALIZATION 4: CORRELATION HEATMAP
# ============================================================

plt.figure()

correlation_matrix = df[
    ["Study_Hours", "Exam_Score"]
].corr()

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="viridis",
    fmt=".2f",
    linewidths=0.5,
    vmin=-1,
    vmax=1
)

plt.title("Correlation Between Study Hours and Exam Scores", pad=15)
plt.tight_layout()
plt.show()

# ============================================================
# 10. VISUALIZATION 5: PERFORMANCE CATEGORY DISTRIBUTION
# ============================================================

performance_order = [
    "Excellent",
    "Good",
    "Needs Improvement"
]

plt.figure()

sns.countplot(
    data=df,
    x="Performance",
    order=performance_order,
    hue="Performance",
    legend=False
)

plt.title("Number of Students by Performance Category", pad=15)
plt.xlabel("Performance Category")
plt.ylabel("Number of Students")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

# ============================================================
# 11. VISUALIZATION 6: AVERAGE SCORE BY CATEGORY
# ============================================================

plt.figure()

sns.barplot(
    data=df,
    x="Performance",
    y="Exam_Score",
    order=performance_order,
    hue="Performance",
    legend=False,
    errorbar=None
)

plt.title("Average Exam Score by Performance Category", pad=15)
plt.xlabel("Performance Category")
plt.ylabel("Average Exam Score")
plt.ylim(0, 100)
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

# ============================================================
# 12. VISUALIZATION 7: COMBINED DASHBOARD
# ============================================================

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

fig.suptitle(
    "Student Performance Analysis Dashboard",
    fontsize=19,
    fontweight="bold",
    y=1.02
)

# Scatter plot: Study hours and exam scores
sns.scatterplot(
    data=df,
    x="Study_Hours",
    y="Exam_Score",
    hue="Performance",
    s=100,
    ax=axes[0, 0]
)

axes[0, 0].set_title("Study Hours vs Exam Scores")
axes[0, 0].set_xlabel("Study Hours")
axes[0, 0].set_ylabel("Exam Score")

# Bar chart: Scores by student
sns.barplot(
    data=df,
    x="Student",
    y="Exam_Score",
    hue="Student",
    legend=False,
    ax=axes[0, 1]
)

axes[0, 1].set_title("Exam Scores by Student")
axes[0, 1].set_xlabel("Student")
axes[0, 1].set_ylabel("Exam Score")
axes[0, 1].set_ylim(0, 100)
axes[0, 1].tick_params(axis="x", rotation=45)

# Histogram: Exam score distribution
sns.histplot(
    data=df,
    x="Exam_Score",
    bins=6,
    kde=True,
    ax=axes[1, 0]
)

axes[1, 0].set_title("Distribution of Exam Scores")
axes[1, 0].set_xlabel("Exam Score")
axes[1, 0].set_ylabel("Number of Students")

# Count plot: Performance categories
sns.countplot(
    data=df,
    x="Performance",
    order=performance_order,
    hue="Performance",
    legend=False,
    ax=axes[1, 1]
)

axes[1, 1].set_title("Student Performance Categories",pad=10 , y=1.0)
axes[1, 1].set_xlabel("Performance Category")
axes[1, 1].set_ylabel("Number of Students")
axes[1, 1].tick_params(axis="x", rotation=15)

plt.tight_layout(rect=[0, 0, 1, 0.93], h_pad=5.0)
plt.show()

# ============================================================
# 13. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 55)
print("                  ANALYSIS COMPLETE")
print("=" * 55)

print("The analysis has generated six individual visualizations")
print("and one combined dashboard.")

print("\nNote:")
print("These results describe the sample dataset of 10 students.")
print("They should not automatically be generalized to all students.")

print("\nThank you for using Student Performance Analysis!")
print("=" * 55)

