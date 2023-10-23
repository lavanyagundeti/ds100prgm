#66


student_scores = (
    ("Alice", 95),
    ("Bob", 88),
    ("Charlie", 92),
    ("David", 78),
    ("Eve", 99),
)


highest_score_student = max(student_scores, key=lambda x: x[1])


highest_score_name, highest_score = highest_score_student


print(f"The student with the highest score is {highest_score_name} with a score of {highest_score}.")
