students = []

def add_student():
    print("\nEnter student details:")
    student = {}
    student['id'] = input("Student ID: ")
    student['name'] = input("Name: ")
    student['age'] = input("Age: ")
    student['grade'] = input("Grade: ")
    student['dob'] = input("Date of Birth (YYYY-MM-DD): ")
    subjects = input("Subjects (comma-separated): ")
    student['subjects'] = [s.strip() for s in subjects.split(',')]
    students.append(student)
    print("\nStudent added successfully!")

def display_all_students():
    print("\n--- Display All Students ---")
    for s in students:
        print(f"Student ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Grade: {s['grade']} | Subjects: {', '.join(s['subjects'])}")
    if not students:
        print("No student records found.")

def update_student():
    sid = input("Enter Student ID to update: ")
    for s in students:
        if s['id'] == sid:
            s['name'] = input("New Name: ")
            s['age'] = input("New Age: ")
            s['grade'] = input("New Grade: ")
            s['dob'] = input("New DOB (YYYY-MM-DD): ")
            subjects = input("New Subjects (comma-separated): ")
            s['subjects'] = [sub.strip() for sub in subjects.split(',')]
            print("Student updated successfully!")
            return
    print("Student not found!")

def delete_student():
    sid = input("Enter Student ID to delete: ")
    for s in students:
        if s['id'] == sid:
            students.remove(s)
            print("Student deleted successfully!")
            return
    print("Student not found!")

def display_subjects_offered():
    all_subjects = set()
    for s in students:
        all_subjects.update(s['subjects'])
    print("\nSubjects Offered:")
    print(", ".join(sorted(all_subjects)) if all_subjects else "No subjects available.")

def main():
    print("Welcome to the Student Data Organizer!")
    while True:
        print("\nSelect an option:")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Update Student Information")
        print("4. Delete Student")
        print("5. Display Subjects Offered")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_all_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            display_subjects_offered()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if_name_ == "_main_" :
    main ()