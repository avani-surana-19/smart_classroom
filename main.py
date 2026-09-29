from array_techniques import find_maximum_score, remove_duplicate_scores, find_kth_smallest_score
from algorithms import compute_summation_and_average, compute_fibonacci_progression
from grading import evaluate_student_grade

def main():
    print("--- SmartClassroom Grade & Performance System ---")
    
    # Sample student marks dataset
    student_marks = [85, 92, 78, 65, 92, 45, 88, 55, 78]
    print(f"Original Marks Record: {student_marks}")
    
    # Clean duplicates using array techniques
    cleaned_marks = remove_duplicate_scores(student_marks)
    print(f"After Removing Duplicate Entries: {cleaned_marks}")
    
    # Compute statistics using fundamental algorithms
    total, avg = compute_summation_and_average(cleaned_marks)
    max_score = find_maximum_score(cleaned_marks)
    print(f"Total Sum: {total} | Class Average: {avg:.2f} | Maximum Score: {max_score}")
    
    # Find kth smallest score
    k = 2
    kth_score = find_kth_smallest_score(cleaned_marks, k)
    print(f"The {k}-nd smallest score in class is: {kth_score}")
    
    print("\n--- Individual Student Evaluations & Suggestions ---")
    for idx, mark in enumerate(cleaned_marks, start=1):
        grade, suggestion = evaluate_student_grade(mark)
        print(f"Student {idx} -> Marks: {mark} | Grade: {grade} | Suggestion: {suggestion}")

if __name__ == "__main__":
    main()