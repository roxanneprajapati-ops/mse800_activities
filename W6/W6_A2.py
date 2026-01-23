import sqlite3


class StudentManager:

    def __init__(self, db_name="students.db"):
        self.db_name = db_name

        # Core dictionary (unchanged idea)
        self.students = {}

        self._init_db()

    def _init_db(self):
        # Create Student table if it does not exist.
        with sqlite3.connect(self.db_name) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS Student (
                    student_id TEXT PRIMARY KEY,
                    student_name TEXT NOT NULL,
                    score INTEGER NOT NULL
                )
            """)

    def add_student(self, student_id, name, score):
        # Add a student to the dictionary.
        self.students[student_id] = {
            "name": name,
            "score": score
        }

    def save_to_db(self):
        # Save to SQLite.
        with sqlite3.connect(self.db_name) as conn:
            for student_id, data in self.students.items():
                conn.execute(
                    "INSERT OR REPLACE INTO Student VALUES (?, ?, ?)",
                    (student_id, data["name"], data["score"])
                )

    def get_top_three(self):
        # Retrieve top 3 students from the database.
        with sqlite3.connect(self.db_name) as conn:
            rows = conn.execute("""
                SELECT student_id, student_name, score
                FROM Student
                ORDER BY score DESC
                LIMIT 3
            """).fetchall()

        # Convert SQL result back to dictionary
        return {
            student_id: {"name": name, "score": score}
            for student_id, name, score in rows
        }

    def display_top_three(self):
        # Print top 3 students
        top_three = self.get_top_three()

        print("\nTop 3 Students:")
        for student_id, info in top_three.items():
            print(f"{student_id} - {info['name']}: {info['score']}")


# ---------------- Example usage ----------------
if __name__ == "__main__":
    manager = StudentManager()
    manager.add_student("S1", "Roxanne", 45)
    manager.add_student("S2", "Albert", 92)
    manager.add_student("S3", "Benj", 78)
    manager.add_student("S4", "Ann", 95)
    manager.add_student("S5", "Earl", 49)
    manager.save_to_db()
    manager.display_top_three()
