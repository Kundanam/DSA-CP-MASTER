from flask import Flask, request, jsonify, render_template
app = Flask(__name__)



class Node:
    def __init__(self, student_id, name, class_no, fees):
        self.student_id = student_id
        self.name = name
        self.class_no = class_no
        self.fees = fees
        self.next = None  # Pointer to the next node
class StudentLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list

    def add_student(self, student_id, name, class_no, fees):
        new_node = Node(student_id, name, class_no, fees)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_student(self, student_id):
        current = self.head
        if not current:
            return "List is empty"

        if current.student_id == student_id:
            self.head = current.next
            return f"Student {student_id} removed"

        while current.next and current.next.student_id != student_id:
            current = current.next

        if current.next:
            current.next = current.next.next
            return f"Student {student_id} removed"
        else:
            return "Student not found"

    def display_students(self):
        students = []
        current = self.head
        while current:
            students.append({
                "id": current.student_id,
                "name": current.name,
                "class_no": current.class_no,
                "fees": current.fees
            })
            current = current.next
        return students



# Initialize the linked list
student_list = StudentLinkedList()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_student', methods=['POST'])
def add_student():
    data = request.json
    student_list.add_student(data['student_id'], data['name'], data['class_no'], data['fees'])
    return jsonify({"message": "Student added successfully"})

@app.route('/display_students', methods=['GET'])
def display_students():
    students = student_list.display_students()
    return jsonify(students)

if __name__ == '__main__':
    app.run(debug=True)


