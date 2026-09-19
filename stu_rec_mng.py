import re

FILE_NAME = "students.txt"


# -----------------------------
# Email Validation
# -----------------------------
def validate_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if re.match(pattern, email):
        return True

    return False


# -----------------------------
# Save Student Data to File
# -----------------------------
def save_student(student):
    try:
        with open(FILE_NAME, "a") as file:
            file.write(
                f"{student['id']},{student['name']},"
                f"{student['age']},{student['email']},"
                f"{student['course']}\n"
            )

        print("\nStudent data saved successfully!")

    except IOError:
        print("\nError: Unable to save student data.")


# -----------------------------
# Add Student
# -----------------------------
def add_student():
    try:
        print("\n========== Add Student ==========")

        student_id = input("Enter Student ID: ").strip()

        if not student_id:
            raise ValueError("Student ID cannot be empty.")

        name = input("Enter Student Name: ").strip()

        if not name:
            raise ValueError("Student name cannot be empty.")

        age = input("Enter Age: ").strip()

        if not age.isdigit():
            raise ValueError("Age must be a number.")

        age = int(age)

        if age <= 0 or age > 100:
            raise ValueError("Age must be between 1 and 100.")

        email = input("Enter Email: ").strip()

        if not validate_email(email):
            raise ValueError("Invalid email address.")

        course = input("Enter Course: ").strip()

        if not course:
            raise ValueError("Course cannot be empty.")

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "email": email,
            "course": course
        }

        save_student(student)

    except ValueError as error:
        print(f"\nInvalid Input: {error}")

    except Exception as error:
        print(f"\nUnexpected error: {error}")


# -----------------------------
# Read Student Data
# -----------------------------
def read_students():
    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()

        if not students:
            print("\nNo student records found.")
            return

        print("\n========== Student Records ==========")

        for student in students:
            data = student.strip().split(",")

            if len(data) == 5:
                print(f"""
Student ID : {data[0]}
Name       : {data[1]}
Age        : {data[2]}
Email      : {data[3]}
Course     : {data[4]}
---------------------------------------
""")

    except FileNotFoundError:
        print("\nNo student data file found.")

    except IOError:
        print("\nError: Unable to read student data.")

    except Exception as error:
        print(f"\nUnexpected error: {error}")


# -----------------------------
# Main Menu
# -----------------------------
def main():
    while True:

        print("""
========================================
       STUDENT RECORD MANAGER
========================================
1. Add Student
2. Read Student Data
3. Exit
========================================
""")

        try:
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                add_student()

            elif choice == "2":
                read_students()

            elif choice == "3":
                print("\nThank you!")
                break

            else:
                raise ValueError("Please enter 1, 2, or 3.")

        except ValueError as error:
            print(f"\nInvalid Input: {error}")

        except KeyboardInterrupt:
            print("\n\nProgram stopped by user.")
            break

        except Exception as error:
            print(f"\nUnexpected error: {error}")


# -----------------------------
# Program Start
# -----------------------------
if __name__ == "__main__":
    main()