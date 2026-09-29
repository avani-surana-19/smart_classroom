# Array Techniques: Finding max, removing duplicates, and finding kth smallest score

def find_maximum_score(scores):
    """Finds the maximum score in a set of student marks."""
    if not scores:
        return None
    max_val = scores[0]
    for score in scores:
        if score > max_val:
            max_val = score
    return max_val

def remove_duplicate_scores(scores):
    """Removes duplicate mark entries from the list."""
    unique_scores = []
    for score in scores:
        if score not in unique_scores:
            unique_scores.append(score)
    return unique_scores

def find_kth_smallest_score(scores, k):
    """Finds the k-th smallest score using sorting techniques."""
    sorted_scores = sorted(scores)
    if k > 0 and k <= len(sorted_scores):
        return sorted_scores[k - 1]
    return None