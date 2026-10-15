
from rapidfuzz import fuzz


def normalize_name(name):
    """Clean a name before comparing it."""
    if not isinstance(name, str):
        raise TypeError("Name must be a string.")

    return " ".join(name.strip().lower().split())


def compare_names(name1, name2):
    """Return a similarity score between two names."""
    first = normalize_name(name1)
    second = normalize_name(name2)

    if not first or not second:
        raise ValueError("Names cannot be empty.")

    score = fuzz.ratio(first, second)

    if score == 100:
        status = "Exact match"
    elif score >= 80:
        status = "Possible match"
    else:
        status = "Low similarity"

    return {
        "name1": name1,
        "name2": name2,
        "score": round(score, 2),
        "status": status,
    }


if __name__ == "__main__":
    first_name = input("Enter first name: ")
    second_name = input("Enter second name: ")

    try:
        result = compare_names(first_name, second_name)
        print("\nComparison result:")
        print(f"Name 1: {result['name1']}")
        print(f"Name 2: {result['name2']}")
        print(f"Similarity: {result['score']}%")
        print(f"Status: {result['status']}")
    except (ValueError, TypeError) as error:
        print(f"Error: {error}")
