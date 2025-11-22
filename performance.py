from storage import Storage

def main():
    st = Storage()

    while True:
        print("\nSTUDENT PERFORMANCE TRACKER")
        print("1. Add Student")
        print("2. Add Marks")
        print("3. View Student")
        print("4. View All Students")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            sid = input("Student ID: ")
            name = input("Student Name: ")
            st.add_student(sid, name)
            print("Student added!")

        elif choice == "2":
            sid = input("Student ID: ")
            score = int(input("Enter marks: "))
            st.add_marks(sid, score)

        elif choice == "3":
            sid = input("Student ID: ")
            student = st.get_student(sid)
            if student:
                print(f"\nName: {student.name}")
                print(f"Marks: {student.marks}")
                print(f"Average: {student.average():.2f}")
            else:
                print("Student not found!")

        elif choice == "4":
            st.show_all()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()