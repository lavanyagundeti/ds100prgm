#26q

student_scores = {
    "Alice": 95,
    "Bob": 87,
    "Charlie": 92,
    "David": 78,
    "Eve": 88
}

total_score = sum(student_scores.values())
num_students = len(student_scores)
average_score = total_score / num_students

print("Average Score:", average_score)
