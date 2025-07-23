class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.total_marks = sum(marks.values())
        self.percentage = self.total_marks / 4        
        self.rank = 0

    def display(self):
        print("--- Student Details ---")
        print("Name: {}".format(self.name))
        print("Marks in 4 subjects: {}".format(self.marks))
        print("Percentage: {}%".format(self.percentage))
        print("Rank: {}".format(self.rank))
        print("-----------------------")

class college:
    def __init__(self):
        self.students = []

    def _update_ranks(self):
        self.students.sort(key=lambda s: s.percentage, reverse=True)
        index = 1
        for s in self.students:
            s.rank = index
            index += 1

    def add_new_student(self):
        name = input("Enter student name: ")
        marks = {
            "Physics":0,
            "Chemistry":0,
            "Maths":0,
            "English":0
        }
        for key, value in marks.items():
            marks[key] = int(input("Enter marks for subject {}: ".format(key)))
        s = student(name, marks)
        self.students.append(s)
        self._update_ranks()
        print("Student '{}' added successfully!".format(name))

    def view_topper(self):
        print("--- Topper ---")
        if not self.students:
            print("No students in the system yet.")
        else:
            topper = self.students[0]
            print("Topper is: {} with {}%".format(topper.name, topper.percentage))

    def view_individual_student_status(self):
        print("--- Individual student Status ---")
        if not self.students:
            print("No students in the system yet.")
            return

        name = input("Enter student name to view status: ")
        student_found = None
        for s in self.students:
            if s.name.lower() == name.lower():
                student_found = s
                break
        
        if student_found:
            student_found.display()
        else:
            print("Student with name '{}' not found.".format(name))

    def status_menu(self):
        while True:
            print("--- Status Menu ---")
            print("1. View Topper")
            print("2. Individual student Status")
            print("3. Back to Main Menu")
            
            choice = input("Enter choice: ")

            if choice == '1':
                self.view_topper()
            elif choice == '2':
                self.view_individual_student_status()
            elif choice == '3':
                break
            else:
                print("Invalid choice, please try again.")

    
    
c = college()
    
while True:
    print("===== Main Menu =====")
    print("1. Add New student")
    print("2. View Status")
    print("3. Exit")
        
    choice = input("Enter choice: ")

    if choice == '1':
        c.add_new_student()
    elif choice == '2':
        c.status_menu()
    elif choice == '3':
        print("Thank you for using our system...")
        break
    else:
        print("Invalid choice... please try again...")