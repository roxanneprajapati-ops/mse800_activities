class Student:
    def __init__(self, student_id, name, score):
        self.student_id = student_id
        self.name = name
        self.score = score

    def has_passed(self, pass_mark=50):
        return self.score >= pass_mark


# Main program
if __name__ == "__main__":
    # List of student object
    students = [
        Student("S001", "Alice", 78),
        Student("S002", "Bob", 45),
        Student("S003", "Charlie", 62),
        Student("S004", "Diana", 49),
        Student("S005", "Ethan", 85),
    ]

    # Part 1:
    # Dictionary {student_id : student_name}
    id_name_dict = {s.student_id: s.name for s in students}
    print(id_name_dict)

    # Dictionary {student_id: student_score}
    id_score_dict = {s.student_id: s.score for s in students}
    print(id_score_dict)


    # combine dictionaries and keep only passed students
    passed_students = {
        student_id: {"name": name, "score": score}
        for (student_id, name), score in zip(
            id_name_dict.items(),
            id_score_dict.values()
        )
        if score >= 50
    }

    # Output
    print("Students who passed MSE800:")
    for student_id, info in passed_students.items():
        print(f"ID: {student_id}, Name: {info['name']}, Score: {info['score']}")
