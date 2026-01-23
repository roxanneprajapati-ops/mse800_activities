class StudentDict:
    def __init__(self, student_names, student_scores):
        # Dictionaries passed in from main
        self.student_names = student_names
        self.student_scores = student_scores

    def get_passed_students(self, pass_mark=50):
        # Combine the two dictionaries and return only students
        # with score above 50
        return {
            student_id: {"name": name, "score": score}
            for (student_id, name), score in zip(
                self.student_names.items(),
                self.student_scores.values()
            )
            if score >= pass_mark
        }


# Main program
if __name__ == "__main__":
    # Part 1: dictionaries creation
    student_names = {
        "S1": "Albert",
        "S2": "Benj",
        "S3": "Roxanne",
        "S4": "Earl",
        "S5": "Ann"
    }

    student_scores = {
        "S1": 78,
        "S2": 45,
        "S3": 62,
        "S4": 49,
        "S5": 85
    }

    records = StudentDict(student_names, student_scores)
    
    # Part 2: combine and filter passed students
    passed_students = records.get_passed_students()
    #print(passed_students)
    print("Top 3 students who passed:")
    for student_id, info in list(passed_students.items())[:3]:
        print(f"ID: {student_id}, Name: {info['name']}, Score: {info['score']}")
