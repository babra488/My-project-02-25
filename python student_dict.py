
class StudentLinkedList:
    def __init__(self):
        self.head = None
    def create_node(self, name, admission, grades):
        return {
            "name": name,
            "admission": admission,
            "grades": grades,  
            "next": None
        }
    def insert(self, name, admission, grades):
        new_node = self.create_node(name, admission, grades)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current["next"] is not None:
            current = current["next"]

        current["next"] = new_node

    # Display all students
    def display(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        print("\n===== STUDENT RECORDS =====\n")
        current = self.head
        while current is not None:
            print(f"Name: {current['name']}")
            print(f"Admission No: {current['admission']}")
            print(f"Grades: {current['grades']}")
            print("-" * 40)
            current = current["next"]
    def search(self, admission):
        current = self.head
        while current is not None:
            if current["admission"] == admission:
                return current
            current = current["next"]
        return None
    def delete(self, admission):
        if self.head is None:
            print("List is empty. Cannot delete.")
            return
        if self.head["admission"] == admission:
            self.head = self.head["next"]
            print(f"Student with admission {admission} deleted.")
            return

        current = self.head
        while current["next"] is not None:
            if current["next"]["admission"] == admission:
                current["next"] = current["next"]["next"]
                print(f"Student with admission {admission} deleted.")
                return
            current = current["next"]

        print(f"No student found with admission number {admission}.")
    def update_grades(self, admission, new_grades):
        student = self.search(admission)
        if student is not None:
            student["grades"] = new_grades
            print(f"Grades updated for student {admission}.")
        else:
            print(f"No student found with admission number {admission}.")

    def count_students(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current["next"]
        return count
students = StudentLinkedList()
students.insert("Alice Akinyi", "ADM001", [78, 84, 90])
students.insert("Brian Mwangi", "ADM002", [67, 74, 81])
students.insert("Caroline Wanjiku", "ADM003", [92, 89, 95])
students.insert("Daniel Otieno", "ADM004", [55, 64, 70])
students.insert("Eva Naliaka", "ADM005", [88, 79, 93])
students.display()
adm_search = "ADM003"
result = students.search(adm_search)
if result:
    print(f"\nFOUND: {result['name']} with grades {result['grades']}\n")
else:
    print("\nStudent not found.\n")
students.update_grades("ADM002", [80, 82, 85])
students.delete("ADM004")
students.display()
print("\nTotal students in list:", students.count_students())

 
    