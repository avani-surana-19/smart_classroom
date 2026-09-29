# Control flow and conditional statements for grading and suggestions

def evaluate_student_grade(percentage):
    """Uses conditional if-elif-else statements to assign grades."""
    if percentage >= 90:
        return 'A', "Excellent performance! Keep tackling advanced problems."
    elif percentage >= 75:
        return 'B', "Good grasp of concepts. Focus on accuracy in intermediate exercises."
    elif percentage >= 60:
        return 'C', "Satisfactory. Review core lectures and practice more problems."
    elif percentage >= 50:
        return 'D', "Needs improvement. Attend extra doubt-clearing sessions."
    else:
        return 'F', "Urgent: Fundamental revision required across all topics."